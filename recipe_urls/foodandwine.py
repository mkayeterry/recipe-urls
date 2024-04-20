from typing import List
import re
from recipe_urls._abstract import AbstractScraper


class FoodAndWineScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.foodandwine\.com/[\w/-]+-\d+")
    UNWANTED_PATTERNS = [
        re.compile(pattern) for pattern in ["how-to", "recipes", "snacks"]
    ]

    @classmethod
    def host(cls):
        return "www.foodandwine.com"
