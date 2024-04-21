import re
from recipe_urls._abstract import AbstractScraper


class WellPlatedScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.wellplated\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "#",
            "best-of",
            "contact",
            "how-to",
            "index",
            "log-in",
            "menu",
            "plan",
            "privacy",
            "recipes",
            "start",
            "work",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.wellplated.com"
