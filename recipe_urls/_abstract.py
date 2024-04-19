from typing import List, Optional
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
}

class AbstractScraper:
    def __init__(self, base_url: Optional[str] = None, html: Optional[str] = None):
        self.base_url = base_url

        if not html:
            try:
                response = requests.get(url=self.base_url, headers=HEADERS)
                response.raise_for_status()

                self.html = response.content
                self.soup = BeautifulSoup(self.html, "html.parser")

            except requests.HTTPError as e:
                if e.response.status_code == 403:
                    raise Exception(f"Access to {self.base_url} is forbidden (403).") from e
                else:
                    raise Exception(f"HTTP error occurred: {e.response.status_code}.") from e
            except requests.RequestException as e:
                raise Exception(f"Request failed: {e}.") from e

            except Exception as e:
                raise Exception(f"Unexpected error accessing {self.base_url}: {e}.") from e

        else:
            self.html = html
            self.soup = BeautifulSoup(self.html, "html.parser")

    @classmethod
    def host(cls) -> Optional[str]:
        raise NotImplementedError("Subclasses must implement the host method.")

    def scrape(self) -> List[str]:
        raise NotImplementedError("Subclasses must implement the scrape method.")
