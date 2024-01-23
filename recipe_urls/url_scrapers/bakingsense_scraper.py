import re
from typing import List
from ..base_scraper import BaseScraper

class BakingSenseScraper(BaseScraper):
    def scrape(self) -> List[str]:
        # Call the base class to get the list of generalized href links
        href_links = super().scrape()

        # Filter href links for recipe-specific ones using site-specific regex
        recipe_links = self.filter_recipe_links(href_links)

        return recipe_links

    def filter_recipe_links(self, href_links: List[str]) -> List[str]:
        print('[bakingsense_scraper.py] Filtering general href links using specififed regex pattern...')

        # Site-specific regex for BakingSense
        recipe_pattern = re.compile(r'https://www\.baking-sense\.com/\d+/\d+/\d+/(?!.*(?:baking-ingredient|baking-ingredients))[\w-]+/')

        # Filter href links for recipe-specific ones
        recipe_links = [link for link in href_links if recipe_pattern.search(link)]

        # Raise an error if no recipe links are found
        if not recipe_links:
            raise ValueError("[bakingsense_scraper.py] No recipe links matched the defined pattern for BakingSense.")

        return recipe_links