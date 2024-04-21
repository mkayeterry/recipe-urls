import re
from recipe_urls._abstract import AbstractScraper


class SallysBakingAddictionScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://sallysbakingaddiction\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "#",
            "catalog",
            "cookbook",
            "how-to",
            "index",
            "tips",
            "tool",
            "trick",
            "update",
            "policy",
            "statement",
            "start-here",
        ]
    ]

    @classmethod
    def host(cls):
        return "sallysbakingaddiction.com"
