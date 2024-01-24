import re
from typing import List
from ..base_scraper import BaseScraper

class BarefootContessaScraper(BaseScraper):
    def scrape(self) -> List[str]:
        # Call the base class to get the list of beautiful soup items
        soup = super().scrape()

        href_links = [a["href"] for a in soup.find_all("a", href=True)]

        if not href_links:
            print(f"[barefootcontessa_scraper.py] Warning: href_links is empty for {self.base_url}")

        # Filter href links for recipe-specific ones using site-specific regex
        recipe_links = self.filter_recipe_links(href_links)

        return recipe_links

    def filter_recipe_links(self, href_links: List[str]) -> List[str]:
        print('[barefootcontessa_scraper.py] Filtering general href links using specififed regex pattern...')

        # Filter out unwanted url patterns
        unwanted_patterns = [
            "breakfast",
            "cocktails",
            "dessert",
            "dinner",
            "lunch",
            "sides",
            "starters"
        ]

        # Site-specific regex for BarefootContessa
        recipe_pattern = re.compile(r'https://barefootcontessa\.com/recipes/[\w-]+/?$')

        # Use a set to deduplicate the links while filtering href links for recipe-specific ones
        unique_links_set = set(link for link in href_links if recipe_pattern.search(link) and not any(re.search(pattern, link) for pattern in unwanted_patterns))

        # Raise an error if no recipe links are found
        if not unique_links_set:
            raise ValueError("[barefootcontessa_scraper.py] No recipe links matched the defined pattern for BarefootContessa.")

        # Convert the set back to a list
        return list(unique_links_set)

