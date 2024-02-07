from typing import List
import re
from recipe_urls._abstract import AbstractScraper

class AmbitiousKitchenScraper(AbstractScraper):
    @classmethod
    def host(cls):
        return "ambitiouskitchen"

    def scrape(self) -> List[str]:
        href_links = [a["href"] for a in self.soup.find_all("a", href=True)]

        if not href_links:
            print(f"[ambitiouskitchen.py] Warning: href_links is empty for {self.base_url}")

        # Filter href links for recipe-specific ones using site-specific regex
        recipe_links = self.filter_links(href_links)

        return recipe_links

    def filter_links(self, href_links: List[str]) -> List[str]:
        
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
            raise ValueError("[ambitiouskitchen.py] No recipe links matched the defined pattern for AmbitiousKitchen.")

        else:
            print(f"{len(unique_links_set)} recipe links found for {self.base_url}.")

        # Convert the set back to a list
        return list(unique_links_set)
