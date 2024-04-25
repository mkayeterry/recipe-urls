import re
from recipe_urls._abstract import AbstractScraper


class Whole30Scraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://whole30\.com/recipes/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
        ]
    ]

    @classmethod
    def host(cls):
        return "whole30.com"