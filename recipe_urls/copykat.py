import re
from recipe_urls._abstract import AbstractScraper


class CopyKatScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://copykat\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "recipes",
        ]
    ]

    @classmethod
    def host(cls):
        return "copykat.com"
