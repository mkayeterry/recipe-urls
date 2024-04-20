from typing import List
import re
from recipe_urls._abstract import AbstractScraper


class EatingWellScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.eatingwell\.com/[\w-]+-\d")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "about",
            "benefit",
            "breakfast",
            "cassie",
            "celebrity",
            "diabetes",
            "dinner",
            "expert",
            "general",
            "inflammation",
            "lunch",
            "maria",
            "matthew",
            "menu",
            "news",
            "philosophy",
            "plan",
            "prep",
            "recall",
            "recipes",
            "review",
            "sell",
            "snack",
            "studies",
            "what",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.eatingwell.com"
