from typing import List
import time
import random
import httpx
from bs4 import BeautifulSoup

class BaseScraper:
    def __init__(self, base_url: str, random_sleeps: bool = True, lower_sleep: int = 1, upper_sleep: int = 3):
        self.base_url = base_url
        self.random_sleeps = random_sleeps
        self.lower_sleep = lower_sleep
        self.upper_sleep = upper_sleep

    def scrape(self) -> List[str]:
        print(f'[base_scraper.py] Scraping {self.base_url}...')

        if self.random_sleeps:
            sleep_time = random.randint(self.lower_sleep, self.upper_sleep)
            time.sleep(sleep_time)

        try:
            response = httpx.get(self.base_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            html = response.content

        except httpx.HTTPError as e:
            print(f"[base_scraper.py] HTTP error for {self.base_url}: {e}")
            return []

        soup = BeautifulSoup(html, "html.parser")

        if not soup:
            print(f"[base_scraper.py] Warning: Soup is empty for {self.base_url}")

        href_links = [a["href"] for a in soup.find_all("a", href=True)]

        if not href_links:
            print(f"[base_scraper.py] Warning: href_links is empty for {self.base_url}")

        return href_links


