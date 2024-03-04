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
            response.raise_for_status()

            self.html = response.content
            self.soup = BeautifulSoup(self.html, "html.parser")

        except (httpx.HTTPError, httpx.ReadTimeout) as e:
            if isinstance(e, httpx.HTTPError) and e.response.status_code == 403:
                raise httpx.HTTPError(f"Access to {self.base_url} is forbidden (403).") from e
            elif isinstance(e, httpx.ReadTimeout):
                raise TimeoutError(f"Request timed out. {self.base_url}") from e
            else:
                raise

        except Exception as e:
            raise RuntimeError(f"Unexpected error accessing {self.base_url}. {e}") from e

    @classmethod
    def host(cls) -> Optional[str]:
        raise NotImplementedError("Subclasses must implement the host method.")

    def scrape(self) -> List[str]:
        raise NotImplementedError("Subclasses must implement the scrape method.")
