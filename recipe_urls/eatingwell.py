from typing import List
import re
from recipe_urls._abstract import AbstractScraper

class EatingWellScraper(AbstractScraper):
    @classmethod
    def host(cls):
        return "eatingwell"

    def scrape(self) -> List[str]:
        try:
            href_links = [a["href"] for a in self.soup.find_all("a", href=True)]
        except Exception as e:
            raise Error(f"Failed to retrieve href_links for {self.base_url}. {str(e)}")

        # Filter href links for recipe-specific ones using site-specific regex
        recipe_links = self.filter_links(href_links)

        return recipe_links

    def filter_links(self, href_links: List[str]) -> List[str]:

        # Filter out unwanted url patterns
        unwanted_patterns = [
            "about", 
            "breakfast", 
            "dinner", 
            "lunch", 
            "menu", 
            "philosophy", 
            "recipes"
        ]

        # Site-specific regex for EatingWell
        recipe_pattern = re.compile(r'https://www\.eatingwell\.com/[\w-]+-\d+$')

        # Use a set to deduplicate the links while filtering href links for recipe-specific ones
        unique_links_set = set(link for link in href_links if recipe_pattern.search(link) and not any(re.search(pattern, link) for pattern in unwanted_patterns))

        # Raise an error if no recipe links are found
        if not unique_links_set:
            raise ValueError("No recipe links matched the defined pattern for EatingWell.")

        else:
            print(f"{len(unique_links_set)} recipe links found for {self.base_url}.")

        # Convert the set back to a list
        return list(unique_links_set)