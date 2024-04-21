import re
from recipe_urls._abstract import AbstractScraper


class HeadbangersKitchenScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://headbangerskitchen\.com/[\w-]+-[\w-]")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "ketosis",
            "how-to",
            "recipes",
            "meal-plan",
            "mistakes",
            "policy",
            "vs",
        ]
    ]

    @classmethod
    def host(cls):
        return "headbangerskitchen.com"
