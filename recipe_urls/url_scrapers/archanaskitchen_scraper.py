import re
from typing import List
from ..base_scraper import BaseScraper

class ArchanasKitchenScraper(BaseScraper):
    def scrape(self) -> List[str]:
        # Call the base class to get the list of beautiful soup items
        soup = super().scrape()

        href_links = [a["href"] for a in soup.find_all("a", href=True)]

        if not href_links:
            print(f"[archanaskitchen_scraper.py] Warning: href_links is empty for {self.base_url}")

        # Filter href links for recipe-specific ones using site-specific regex
        recipe_links = self.filter_recipe_links(href_links)

        return recipe_links

    def filter_recipe_links(self, href_links: List[str]) -> List[str]:
        print('[archanaskitchen_scraper.py] Filtering general href links using specififed regex pattern...')

        # Filter out unwanted url patterns
        unwanted_patterns = [
            "about",
            "archana-s-kitchen",
            "articles",
            "brands",
            "breakfast",
            "careers",
            "collections", 
            "contact",
            "dinner",
            "ideas",
            "lunch",
            "meal",
            "media",
            "partners",
            "privacy",
            "recipes",
            "team",
            "terms",
            "values",
            "videos",
        ]


        # Site-specific regex for ArchanasKitchen
        recipe_pattern = re.compile(r'/([\w-]+)/?$')

        # Use a set to deduplicate the links while filtering href links for recipe-specific ones
        unique_links_set = set("https://www.archanaskitchen.com{}".format(link) for link in href_links if recipe_pattern.search(link) and not any(re.search(pattern, link) for pattern in unwanted_patterns))

        # Raise an error if no recipe links are found
        if not unique_links_set:
            raise ValueError("[archanaskitchen_scraper.py] No recipe links matched the defined pattern for ArchanasKitchen.")

        # Convert the set back to a list
        return list(unique_links_set)

