import re
from recipe_urls._abstract import AbstractScraper


class BettyCrockerScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/recipes+/[\w-]+-[\w-]+/[\d\w]")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "cuisine",
            "health",
            "main-ingredient",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.bettycrocker.com"
