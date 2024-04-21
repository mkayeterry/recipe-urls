import re
from recipe_urls._abstract import AbstractScraper


class FitSlowCookerQueenScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://fitslowcookerqueen\.com/[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern) for pattern in ["about", "category", "guide", "page"]
    ]

    @classmethod
    def host(cls):
        return "fitslowcookerqueen.com"
