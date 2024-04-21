import re
from recipe_urls._abstract import AbstractScraper


class EatingBirdFoodScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.eatingbirdfood\.com/[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "about",
            "baby",
            "babies",
            "category",
            "cookbook",
            "policy",
            "recipes",
            "shop",
            "tag",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.eatingbirdfood.com"
