from typing import List
import re
from recipe_urls._abstract import AbstractScraper

class EatSmarterScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r'/recipes/[\w-]+[\w-]')
    UNWANTED_PATTERNS = [re.compile(pattern) for pattern in [
            "baking", 
            "cooking", 
            "cookbooks", 
            "eatsmarter", 
            "ingredients",
            "menu",  
            "nutritional",
            "regional",  
            "seasonal", 
            "special"
        ]]
    @classmethod
    def host(cls):
        return "eatsmarter.com"

    def scrape(self) -> List[str]:
        try:
            href_links = [a["href"] for a in self.soup.find_all("a", href=True, attrs={"class": "teaser-wrapper-link"})]
        except Exception as e:
            print(f"[eatsmarter.py] Error: href_links is empty for {self.base_url}")
            raise e
