import re
from recipe_urls._abstract import AbstractScraper


class ArchanasKitchenScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/[\w-]+-[\w-]")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "about",
            "archana-s-kitchen",
            "articles",
            "brands",
            "breakfast",
            "careers",
            "collections",
            "contact",
            "dinner",
            "home", 
            "ideas",
            "lunch",
            "meal",
            "media",
            "partners",
            "privacy",
            "recipes",
            "team",
            "terms",
            "values",
            "videos",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.archanaskitchen.com"
