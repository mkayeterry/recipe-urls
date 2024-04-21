import re
from recipe_urls._abstract import AbstractScraper


class HandleTheHeatScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://handletheheat\.com/[\w-]+-[\w-]")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in ["about", "how-to", "recipes", "science", "vs"]
    ]

    @classmethod
    def host(cls):
        return "handletheheat.com"
