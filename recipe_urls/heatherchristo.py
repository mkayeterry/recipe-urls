import re
from recipe_urls._abstract import AbstractScraper


class HeatherChristoScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(
        r"https://heatherchristo\.com/\d{4}/\d{2}/\d{2}/[\w-]+-[\w-]+/"
    )
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "category",
            "contact",
            "library",
            "press",
            "policy",
            "recipes",
            "serena",
            "shop",
            "work-with-me",
        ]
    ]

    @classmethod
    def host(cls):
        return "heatherchristo.com"
