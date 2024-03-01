from typing import List, Optional
import time
import random
import httpx
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
}

class AbstractScraper:
    def __init__(self, base_url: str, random_sleeps: bool = True, lower_sleep: int = 1, upper_sleep: int = 3):
        self.base_url = base_url
        self.random_sleeps = random_sleeps
        self.lower_sleep = lower_sleep
        self.upper_sleep = upper_sleep

        if random_sleeps:
            sleep_time = random.randint(self.lower_sleep, self.upper_sleep)
            time.sleep(sleep_time)

        try:
            response = httpx.get(url=self.base_url, headers=HEADERS)

            self.html = response.content
            self.soup = BeautifulSoup(self.html, "html.parser")

        except httpx.HTTPError as e:
            raise httpx.HTTPError(f"HTTP error for {self.base_url}. {e}") from e

        except Exception as e:
            raise RuntimeError(f"Unexpected error accessing {self.base_url}. {e}") from e

    @classmethod
    def host(cls) -> Optional[str]:
        raise NotImplementedError("Subclasses must implement the host method.")

    def scrape(self) -> List[str]:
        raise NotImplementedError("Subclasses must implement the scrape method.")


import re

base_url = 'https://www.foodandwine.com/recipes'

response = httpx.get(url = base_url, headers = HEADERS)
response.raise_for_status()
html = response.content
soup = BeautifulSoup(html, "html.parser")
href_links = [a["href"] for a in soup.find_all(string=re.compile("mntl-card-list-items"), href=True)]

# Site-specific regex for Cookpad
recipe_pattern = re.compile(r'https://www\.foodandwine\.com/[\w/-]+-\d+')

# Use a set to deduplicate the links while filtering href links for recipe-specific ones
unique_links_set = set(link for link in href_links if recipe_pattern.search(link))