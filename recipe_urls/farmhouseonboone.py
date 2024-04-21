import re
from recipe_urls._abstract import AbstractScraper


class FarmhouseOnBooneScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.farmhouseonboone\.com/[\w-]+[\w-]")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "best",
            "category",
            "diy",
            "facial",
            "face",
            "how-to",
            "index",
            "masterclass",
            "make",
            "meet",
            "policy",
            "series",
            "tag",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.farmhouseonboone.com"
