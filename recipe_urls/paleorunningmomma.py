import re
from recipe_urls._abstract import AbstractScraper


class PaleoRunningMommaScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.paleorunningmomma\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "about",
            "baking",
            "contact",
            "disclaimer",
            "recipes",
            "policy",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.paleorunningmomma.com"
