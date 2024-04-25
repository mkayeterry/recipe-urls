import re
from recipe_urls._abstract import AbstractScraper


class SimpleVeganistaScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://simple-veganista\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "index", 
            "vs"
        ]
    ]

    @classmethod
    def host(cls):
        return "simple-veganista.com"
