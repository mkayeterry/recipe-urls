from recipe_urls._abstract import AbstractScraper
import re


class AbuelasCounterScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://abuelascounter\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in ["index", "must-haves", "newsletter", "policy"]
    ]

    @classmethod
    def host(cls):
        return "abuelascounter.com"
