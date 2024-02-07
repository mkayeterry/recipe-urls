from typing import List
import re
from recipe_urls._abstract import AbstractScraper

class AverieCooksScraper(AbstractScraper):
    @classmethod
    def host(cls):
        return "averiecooks"

    def scrape(self) -> List[str]:
        href_links = [a["href"] for a in self.soup.find_all("a", href=True)]

        if not href_links:
            print(f"[averiecooks.py] Warning: href_links is empty for {self.base_url}")

        # Filter href links for recipe-specific ones using site-specific regex
        recipe_links = self.filter_links(href_links)

        return recipe_links

    def filter_links(self, href_links: List[str]) -> List[str]:
        
        # Filter out unwanted url patterns
        unwanted_patterns = [
            "interview-with-averie", 
            "work-with-me"
        ]

        # Site-specific regex for AverieCooks
        recipe_pattern = re.compile(r'https://www\.averiecooks\.com/([a-zA-Z]+-){2,}[a-zA-Z]+/')

        # Use a set to deduplicate the links while filtering href links for recipe-specific ones
        unique_links_set = set(link for link in href_links if recipe_pattern.search(link) and not any(re.search(pattern, link) for pattern in unwanted_patterns))

        # Raise an error if no recipe links are found
        if not unique_links_set:
            raise ValueError("[averiecooks.py] No recipe links matched the defined pattern for AverieCooks.")

        else:
            print(f"{len(unique_links_set)} recipe links found for {self.base_url}.")

        # Convert the set back to a list
        return list(unique_links_set)
