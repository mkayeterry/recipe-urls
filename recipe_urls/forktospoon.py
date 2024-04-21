import re
from recipe_urls._abstract import AbstractScraper


class ForkToSpoonScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://forktospoon\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "category",
            "contact",
            "cookbook",
            "how",
            "method",
            "policy",
            "weekly",
            "what",
        ]
    ]

    @classmethod
    def host(cls):
        return "forktospoon.com"
