import re
from recipe_urls._abstract import AbstractScraper


class LivelyTableScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://livelytable\.com/[\w/-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "about",
            "benefits",
            "category",
            "conversions",
            "conditions",
            "diet",
            "does",
            "healthiest",
            "how-to",
            "living",
            "methods",
            "recipes",
            "substitute",
            "types",
        ]
    ]

    @classmethod
    def host(cls):
        return "livelytable.com"
