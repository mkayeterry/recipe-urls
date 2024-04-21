import re
from recipe_urls._abstract import AbstractScraper


class BudgetBytesScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.budgetbytes\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "basics",
            "how-to",
            "ideas",
            "policy",
            "recipes",
            "recipe",
            "terms",
            "welcome",
            "videos",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.budgetbytes.com"
