import re
from recipe_urls._abstract import AbstractScraper


class GoodHousekeepingScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/food-recipes/[\d\w-]+/[\w-]+-[\w-]+recipe/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "goodhousekeeping",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.goodhousekeeping.com"
