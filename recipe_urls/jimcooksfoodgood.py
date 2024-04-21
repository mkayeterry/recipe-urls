import re
from recipe_urls._abstract import AbstractScraper


class JimCooksFoodGoodScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://jimcooksfoodgood\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "about",
            "cookbook",
            "recipes",
        ]
    ]

    @classmethod
    def host(cls):
        return "jimcooksfoodgood.com"
