import re
from recipe_urls._abstract import AbstractScraper


class LovingItVeganScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://lovingitvegan\.com/[\w/-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "about",
            "category",
            "contact",
            "ebook",
            "how",
            "recipes",
            "terms",
            "policy",
        ]
    ]

    @classmethod
    def host(cls):
        return "lovingitvegan.com"
