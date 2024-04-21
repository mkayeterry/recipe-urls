import re
from recipe_urls._abstract import AbstractScraper


class LifestyleOfAFoodieScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://lifestyleofafoodie\.com/[\w/-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "about",
            "category",
            "collection",
            "contact",
            "policy",
            "recipes",
        ]
    ]

    @classmethod
    def host(cls):
        return "lifestyleofafoodie.com"
