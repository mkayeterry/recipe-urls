import re
from recipe_urls._abstract import AbstractScraper


class TasteOfHomeScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.tasteofhome\.com/recipes/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "cooking-style",
            "type",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.tasteofhome.com"
