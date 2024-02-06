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
            response = httpx.get(url = self.base_url, headers = HEADERS)
            response.raise_for_status()

            self.html = response.content
            self.soup = BeautifulSoup(self.html, "html.parser")
        
        except httpx.HTTPError as e:
            print(f"[_abstract.py] HTTP error for {self.base_url}: {e}")

    @classmethod
    def host(cls) -> str:
        raise NotImplementedError("[_abstract.py] This should be implemented.")
        
    def scrape(self) -> List[str]:
        raise NotImplementedError("[_abstract.py] Subclasses must implement the scrape method.")
