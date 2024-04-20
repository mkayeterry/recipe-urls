import re
from recipe_urls._abstract import AbstractScraper


class BowlOfDeliciousScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.bowlofdelicious\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "how-to",
            "reports",
            "why",
            "privacy",
            "work-with-me",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.bowlofdelicious.com"
