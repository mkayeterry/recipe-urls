import re
from recipe_urls._abstract import AbstractScraper


class EatingWellScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.eatingwell\.com/[\w-]+-\d")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "about",
            "benefit",
            "best", 
            "breakfast",
            "cassie",
            "celebrity",
            "diabetes",
            "dinner",
            "does", 
            "drew", 
            "expert",
            'favorite', 
            "general",
            "good-for", 
            "inflammation",
            "interview", 
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
            "sneaker", 
            "start", 
            "studies",
            "what",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.eatingwell.com"
