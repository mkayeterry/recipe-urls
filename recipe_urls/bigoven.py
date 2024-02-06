from typing import List
import re
from recipe_urls._abstract import AbstractScraper

class BigOvenScraper(AbstractScraper):
    @classmethod
    def host(cls):
        return "bigoven"

    def scrape(self) -> List[str]:
        href_links = [a["href"] for a in self.soup.find_all("a", href=True)]

        if not href_links:
            print(f"[bigoven.py] Warning: href_links is empty for {self.base_url}")

        # Filter href links for recipe-specific ones using site-specific regex
        recipe_links = self.filter_links(href_links)

        return recipe_links

    def filter_links(self, href_links: List[str]) -> List[str]:

        # Filter out unwanted url patterns
        unwanted_patterns = [
            "#reviews-section"
        ]

        # Site-specific regex for BigOven
        recipe_pattern = re.compile(r'/recipe/([^/]+)/(\d+)')

        # Use a set to deduplicate the links while filtering href links for recipe-specific ones
        unique_links_set = set("https://www.bigoven.com{}".format(link) for link in href_links if recipe_pattern.search(link) and not any(re.search(pattern, link) for pattern in unwanted_patterns))

        # Raise an error if no recipe links are found
        if not unique_links_set:
            raise ValueError("[bigoven.py] No recipe links matched the defined pattern for BigOven.")

        else:
            print(f"[bigoven.py] {len(unique_links_set)} recipe links found for {self.base_url}.")

        # Convert the set back to a list
        return list(unique_links_set)