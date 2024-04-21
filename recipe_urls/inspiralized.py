import re
from recipe_urls._abstract import AbstractScraper


class InspiralizedScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://inspiralized\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "by-spiralized",
            "category",
            "index",
            "ingredient",
            "how-to",
            "meal-type",
            "privacy",
        ]
    ]

    @classmethod
    def host(cls):
        return "inspiralized.com"
