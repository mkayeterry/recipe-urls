from typing import List
import re
from recipe_urls._abstract import AbstractScraper


class ACoupleCooksScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://abuelascounter\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "appetizers",
            "best",
            "breakfast",
            "cooking",
            "contact",
            "dinner",
            "dinners",
            "dishes",
            "desserts",
            "guide",
            "how",
            "ideas",
            "lunch",
            "meal-plan",
            "recipes",
            "skills",
            "snacks",
            "statement",
            "things",
            "party",
            "policy",
            "why",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.acouplecooks.com"
