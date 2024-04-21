import re
from recipe_urls._abstract import AbstractScraper


class CreativeCanningScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://creativecanning\.com/[\w-]+/$")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "about",
            "canning-",
            "policy",
        ]
    ]

    @classmethod
    def host(cls):
        return "creativecanning.com"
