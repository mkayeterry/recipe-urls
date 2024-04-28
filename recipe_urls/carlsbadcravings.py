import re
from recipe_urls._abstract import AbstractScraper


class CarlsbadCravingsScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://carlsbadcravings\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "contact",
            "how-to", 
            "latest",
            "privacy",
        ]
    ]

    @classmethod
    def host(cls):
        return "carlsbadcravings.com"
