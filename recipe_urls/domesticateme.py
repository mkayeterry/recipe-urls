import re
from recipe_urls._abstract import AbstractScraper


class DomesticateMeScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://domesticate-me\.com/[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "category",
            "classes", 
            "contact",
            "dude", 
            "faq", 
            "gift", 
            "library",
            "press",
            "policy",
            "recipes",
            "sides", 
            "search", 
            "serena",
            "shop",
            "work-with-me",
        ]
    ]

    @classmethod
    def host(cls):
        return "domesticate-me.com"
