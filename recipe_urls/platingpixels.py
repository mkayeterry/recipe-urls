import re
from recipe_urls._abstract import AbstractScraper


class PlatingPixelsScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.platingpixels\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "how-to",
            "policy",
            "work",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.platingpixels.com"
