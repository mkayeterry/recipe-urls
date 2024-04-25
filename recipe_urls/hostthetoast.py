import re
from recipe_urls._abstract import AbstractScraper


class HostTheToastScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://hostthetoast\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "about-us",
            "how-to"
        ]
    ]

    @classmethod
    def host(cls):
        return "hostthetoast.com"
