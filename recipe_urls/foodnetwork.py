import re
from recipe_urls._abstract import AbstractScraper


class FoodNetworkScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(
        r"https://www\.foodnetwork\.com/recipes/food-network-kitchen/[\w-]+-[\w-]+\d"
    )
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "category",
            "contact",
            "library",
            "press",
            "policy",
            "recipes",
            "serena",
            "shop",
            "work-with-me",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.foodnetwork.com"
