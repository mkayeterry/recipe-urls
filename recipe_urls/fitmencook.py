import re
from recipe_urls._abstract import AbstractScraper


class FitMenCookScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://fitmencook\.com/recipes/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "=",
        ]
    ]

    @classmethod
    def host(cls):
        return "fitmencook.com"
