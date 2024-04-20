import re
from recipe_urls._abstract import AbstractScraper


class OhSheGlowsScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://ohsheglows\.com/[\w/-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "about",
            "app",
            "archives",
            "book",
            "categories",
            "news",
            "skin",
            "tools",
            "search",
        ]
    ]

    @classmethod
    def host(cls):
        return "ohsheglows.com"
