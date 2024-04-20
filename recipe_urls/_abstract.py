from typing import List, Optional
import re
import requests
from requests.exceptions import HTTPError, RequestException
from bs4 import BeautifulSoup

class AbstractScraper:
    RECIPE_PATTERN = None
    UNWANTED_PATTERNS = []

    def __init__(self, base_url: Optional[str] = None, html: Optional[str] = None):
        self.base_url = base_url
        if not html:
            try:
                response = requests.get(url=self.base_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"})
                response.raise_for_status()
                self.html = response.content
                self.soup = BeautifulSoup(self.html, "html.parser")
            except HTTPError as e:
                if e.response.status_code == 403:
                    raise Exception(f"Access to {self.base_url} is forbidden (403).") from e
                else:
                    raise Exception(f"HTTP error occurred: {e.response.status_code}.") from e
            except RequestException as e:
                raise Exception(f"Request failed: {e}.") from e
            except Exception as e:
                raise Exception(f"Unexpected error accessing {self.base_url}: {e}.") from e
        else:
            self.html = html
            self.soup = BeautifulSoup(self.html, "html.parser")

    def scrape(self) -> List[str]:
        try:
            href_links = [a["href"] for a in self.soup.find_all("a", href=True)]
        except (TypeError, AttributeError) as e:
            raise ValueError(f"Failed to extract href links: {e}") from e
        return self.filter_links(href_links)

    def filter_links(self, href_links: List[str]) -> List[str]:
        unique_links = {link for link in href_links if self.is_recipe_link(link)}
        return list(unique_links)

    def is_recipe_link(self, link: str) -> bool:
        if self.RECIPE_PATTERN and self.RECIPE_PATTERN.search(link):
            return not any(pattern.search(link) for pattern in self.UNWANTED_PATTERNS)
        return False
