import re
from recipe_urls._abstract import AbstractScraper


class ErrensKitchenScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.errenskitchen\.com/[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "about",
            "all-posts",
            "category",
            "contact",
            "conversions",
            "philosophy",
            "policy",
            "recipes",
            "videos",
            "welcome",
            "work-with-me",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.errenskitchen.com"
