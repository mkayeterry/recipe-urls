import re
from recipe_urls._abstract import AbstractScraper


class LeanAndGreenRecipesScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/recipes/[\w-]+/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "category",
            "tags",
        ]
    ]

    @classmethod
    def host(cls):
        return "leanandgreenrecipes.net"
