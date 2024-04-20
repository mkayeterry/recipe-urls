import re
from recipe_urls._abstract import AbstractScraper


class EatWhatTonightScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://eatwhattonight\.com/\d{4}/\d{2}/[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "recipes",
        ]
    ]

    @classmethod
    def host(cls):
        return "eatwhattonight.com"
