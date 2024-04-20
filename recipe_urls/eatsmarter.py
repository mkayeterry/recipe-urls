import re
from recipe_urls._abstract import AbstractScraper


class EatSmarterScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/recipes/[\w-]+[\w-]")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "baking",
            "cooking",
            "cookbooks",
            "eatsmarter",
            "ingredients",
            "menu",
            "nutritional",
            "regional",
            "seasonal",
            "special",
        ]
    ]
    CUSTOM_HREF = ("a", {"class": "teaser-wrapper-link"})

    @classmethod
    def host(cls):
        return "eatsmarter.com"
