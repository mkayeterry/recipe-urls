import re
from recipe_urls._abstract import AbstractScraper


class ChefSavvyScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://chefsavvy\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "ideas",
            "dishes",
            "ebook",
            "meals",
            "policy",
            "recipes",
            "recipe-type",
        ]
    ]

    @classmethod
    def host(cls):
        return "chefsavvy.com"
