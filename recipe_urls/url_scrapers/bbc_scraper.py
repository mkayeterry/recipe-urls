import re
from typing import List
from ..base_scraper import BaseScraper

class BBCScraper(BaseScraper):
    def scrape(self) -> List[str]:
        # Call the base class to get the list of beautiful soup items
        soup = super().scrape()

        href_links = [a["href"] for a in soup.find_all("a", href=True)]

        if not href_links:
            print(f"[bbc_scraper.py] Warning: href_links is empty for {self.base_url}")

        # Filter href links for recipe-specific ones using site-specific regex
        recipe_links = self.filter_recipe_links(href_links)

        return recipe_links

    def filter_recipe_links(self, href_links: List[str]) -> List[str]:
        print('[bbc_scraper.py] Filtering general href links using specififed regex pattern...')

        # Site-specific regex for BBC
        recipe_pattern = re.compile(r'/food/recipes/([^/]+)')

        # Use a set to deduplicate the links while filtering href links for recipe-specific ones
        unique_links_set = set("https://www.bbc.co.uk{}".format(link) for link in href_links if recipe_pattern.search(link))

        # Raise an error if no recipe links are found
        if not unique_links_set:
            raise ValueError("[bbc_scraper.py] No recipe links matched the defined pattern for BBC.")

        # Convert the set back to a list
        return list(unique_links_set)
