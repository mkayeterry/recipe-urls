import re
from recipe_urls._abstract import AbstractScraper


class AmbitiousKitchenScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.ambitiouskitchen\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "ambitious-home",
            "ambitious-mama",
            "appetizer",
            "appetizers",
            "breakfast",
            "cooking",
            "dessert",
            "diet",
            "discount-codes",
            "dinner",
            "dinners",
            "drinks",
            "grocery",
            "how-to",
            "kid-friendly",
            "lifestyle",
            "lunch",
            "lunches",
            "meals",
            "natural",
            "party",
            "privacy-policy",
            "recipe",
            "recipes",
            "snack",
            "snacks",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.ambitiouskitchen.com"
