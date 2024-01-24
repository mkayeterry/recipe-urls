import re
from typing import List
from ..base_scraper import BaseScraper

class AmbitiousKitchenScraper(BaseScraper):
    def scrape(self) -> List[str]:
        # Call the base class to get the list of beautiful soup items
        soup = super().scrape()

        href_links = [a["href"] for a in soup.find_all("a", href=True)]

        if not href_links:
            print(f"[ambitiouskitchen_scraper.py] Warning: href_links is empty for {self.base_url}")

        # Filter href links for recipe-specific ones using site-specific regex
        recipe_links = self.filter_recipe_links(href_links)

        return recipe_links

    def filter_recipe_links(self, href_links: List[str]) -> List[str]:
        print('[ambitiouskitchen_scraper.py] Filtering general href links using specififed regex pattern...')

        # Filter out unwanted url patterns
        unwanted_patterns = [
            "ambitious-home",
            "ambitious-mama",
            "appetizer",
            "appetizers",
            "breakfast",
            "cooking",
            "dessert",
            "diet",
            "discount-codes",
            "dinner",
            "dinners",
            "drinks",
            "grocery",
            "how-to",
            "kid-friendly",
            "lifestyle",
            "lunch",
            "lunches",
            "meals",
            "party",
            "privacy-policy",
            "recipe",
            "recipes",
            "snack",
            "snacks"
        ]

        # Site-specific regex for AmbitiousKitchen
        recipe_pattern = re.compile(r'https://www\.ambitiouskitchen\.com/([a-zA-Z]+-){2,}[a-zA-Z]+/')

        # Use a set to deduplicate the links while filtering href links for recipe-specific ones
        unique_links_set = set(link for link in href_links if recipe_pattern.search(link) and not any(re.search(pattern, link) for pattern in unwanted_patterns))

        # Raise an error if no recipe links are found
        if not unique_links_set:
            raise ValueError("[ambitiouskitchen_scraper.py] No recipe links matched the defined pattern for AmbitiousKitchen.")

        # Convert the set back to a list
        return list(unique_links_set)