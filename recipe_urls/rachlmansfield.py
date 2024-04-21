import re
from recipe_urls._abstract import AbstractScraper


class RachlMansfieldScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(
        r"https://rachlmansfield\.com/(?![\w-]*\d)[\w-]+-[\w-]+/"
    )
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "discount",
            "guide",
            "home",
            "mom",
            "must-have",
            "policy",
            "pregnancy",
            "tips",
            "what",
        ]
    ]

    @classmethod
    def host(cls):
        return "rachlmansfield.com"
