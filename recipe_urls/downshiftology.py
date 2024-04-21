import re
from recipe_urls._abstract import AbstractScraper


class DownshiftologyScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://downshiftology\.com/recipes/[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "how-to",
        ]
    ]

    @classmethod
    def host(cls):
        return "downshiftology.com"
