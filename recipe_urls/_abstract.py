from typing import List, Optional
import requests
from requests.exceptions import HTTPError, RequestException
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from recipe_urls._utils import extract_base_domain, concat_host


class AbstractScraper:
    RECIPE_PATTERN = None
    UNWANTED_PATTERNS = []
    CUSTOM_HREF = ("a", {"href": True})


    def __init__(self, base_url: Optional[str] = None, html: Optional[str] = None):
        self.base_url = base_url

        if not html:
            try:
                response = requests.get(
                    url=self.base_url,
                    headers={
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
                    },
                )
                response.raise_for_status()
                self.html = response.content
                self.soup = BeautifulSoup(self.html, "html.parser")

            except HTTPError as e:
                if e.response.status_code == 403:
                    raise Exception(
                        f"Access to {self.base_url} is forbidden (403)."
                    ) from e
                else:
                    raise Exception(
                        f"HTTP error occurred: {e.response.status_code}."
                    ) from e

            except RequestException as e:
                raise Exception(f"Request failed: {e}.") from e

            except Exception as e:
                raise Exception(
                    f"Unexpected error accessing {self.base_url}: {e}."
                ) from e
        else:
            self.html = html
            self.soup = BeautifulSoup(self.html, "html.parser")


    def scrape(self) -> List[str]:

        try:
            tag, attrs = self.CUSTOM_HREF
            attrs["href"] = True
            href_links = [a["href"] for a in self.soup.find_all(tag, attrs)]

        except (TypeError, AttributeError) as e:
            raise ValueError(f"Failed to extract href links: {e}") from e

        unique_links = {concat_host(link, self.base_url, self.soup) for link in href_links 
                            if self.RECIPE_PATTERN and self.RECIPE_PATTERN.search(link) 
                            and not any(pattern.search(link) for pattern in self.UNWANTED_PATTERNS)}

        return list(unique_links)

        





