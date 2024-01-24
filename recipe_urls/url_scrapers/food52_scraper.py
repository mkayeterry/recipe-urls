import re
from typing import List
from ..base_scraper import BaseScraper

class Food52Scraper(BaseScraper):
    def scrape(self) -> List[str]:
        # Call the base class to get the list of beautiful soup items
        soup = super().scrape()

        href_links = [a["href"] for a in soup.find_all("a", href=True)]

        if not href_links:
            print(f"[food52_scraper.py] Warning: href_links is empty for {self.base_url}")

        # Filter href links for recipe-specific ones using site-specific regex
        recipe_links = self.filter_recipe_links(href_links)

        return recipe_links

    def filter_recipe_links(self, href_links: List[str]) -> List[str]:
        print('[food52_scraper.py] Filtering general href links using specififed regex pattern...')

        # Site-specific regex for Food52
        recipe_pattern = re.compile(r'/recipes/([^/]+)')

        # Filter href links for recipe-specific ones
        recipe_links = ["https://www.food52.com{}".format(link) for link in href_links if recipe_pattern.search(link)]

        # Raise an error if no recipe links are found
        if not recipe_links:
            raise ValueError("[food52_scraper.py] No recipe links matched the defined pattern for Food52.")

        return recipe_links