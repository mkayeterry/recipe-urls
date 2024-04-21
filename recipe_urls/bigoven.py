import re
from recipe_urls._abstract import AbstractScraper


class BigOvenScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/recipe/[\w-]+-[\w-]+/\d")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "#",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.bigoven.com"
