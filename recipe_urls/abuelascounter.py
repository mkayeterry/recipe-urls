from typing import List, Set
import re
from recipe_urls._abstract import AbstractScraper

class AbuelasCounterScraper(AbstractScraper):
    # Precompile regex patterns
    RECIPE_PATTERN = re.compile(r'https://abuelascounter\.com/[\w-]+-[\w-]+/')
    UNWANTED_PATTERNS = [
        re.compile(pattern) for pattern in ["index", "must-haves", "newsletter", "policy"]
    ]

    @classmethod
    def host(cls):
        return "abuelascounter.com"

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
        if self.RECIPE_PATTERN.search(link):
            return not any(pattern.search(link) for pattern in self.UNWANTED_PATTERNS)
        return False
