import re
from recipe_urls._abstract import AbstractScraper


class GonnaWantSecondsScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.gonnawantseconds\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern) for pattern in ["contact", "index", "user"]
    ]

    @classmethod
    def host(cls):
        return "www.gonnawantseconds.com"
