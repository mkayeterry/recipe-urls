import re
from recipe_urls._abstract import AbstractScraper


class IzzyCookingScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://izzycooking\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in ["about", "contact", "how-to", "policy", "recipe-index"]
    ]

    @classmethod
    def host(cls):
        return "izzycooking.com"
