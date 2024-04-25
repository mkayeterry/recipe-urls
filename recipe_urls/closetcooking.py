import re
from recipe_urls._abstract import AbstractScraper


class ClosetCookingScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.closetcooking\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "best-of",
            "ecookbook",
            "index",
            "recipes", 
            "#",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.closetcooking.com"
