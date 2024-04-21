import re
from recipe_urls._abstract import AbstractScraper


class ImWorthyScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://im-worthy\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "recipes",
        ]
    ]

    @classmethod
    def host(cls):
        return "im-worthy.com"
