import re
from recipe_urls._abstract import AbstractScraper


class DavidLebovitzScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.davidlebovitz\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "#",
            "category",
            "policy",
            "statement",
            "terms",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.davidlebovitz.com"
