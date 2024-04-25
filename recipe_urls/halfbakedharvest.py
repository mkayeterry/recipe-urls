import re
from recipe_urls._abstract import AbstractScraper


class HalfbakedHarvestScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.halfbakedharvest\.com/(?!\d)[\w-]+-[\w-]")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "accessibility",
            "archives",
            "available",
            "collections",
            "favorite-things",
            "index",
            "log-in",
            "policy",
            "tieghan",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.halfbakedharvest.com"
