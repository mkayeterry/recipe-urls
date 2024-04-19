from typing import List
import re
from recipe_urls._abstract import AbstractScraper

class AfghanKitchenRecipesScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r'https://www\.afghankitchenrecipes\.com/recipe/[\w-]+/')

    @classmethod
    def host(cls):
        return "www.afghankitchenrecipes.com"

    def scrape(self) -> List[str]:
        try:
            href_links = [a["href"] for a in self.soup.find_all("a", href=True)]
        except (TypeError, AttributeError) as e:
            raise ValueError(f"Failed to extract href links: {e}") from e

        return self.filter_links(href_links)

    def filter_links(self, href_links: List[str]) -> List[str]:
        # Use a set to deduplicate the links while filtering href links for recipe-specific ones
        unique_links_set = set(link for link in href_links if self.RECIPE_PATTERN.search(link))

        return list(unique_links_set)
