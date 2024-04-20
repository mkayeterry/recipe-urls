from typing import List
import re
from recipe_urls._abstract import AbstractScraper


class CdKitchenScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(
        r"https://www\.cdkitchen\.com/recipes/[\w-]+/\d+/[\w-]+[\w-]+\.shtml"
    )
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "category",
            "can",
            "options",
            "recipes",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.cdkitchen.com"
