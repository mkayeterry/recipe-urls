import re
from recipe_urls._abstract import AbstractScraper


class FifteenSpatulasScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.fifteenspatulas\.com/[\w-]+/$")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "all", 
            "contact", 
            "index",
            "meals",  
            "press", 
            "policy", 
            "side", 
            "terms", 
            "travel"
        ]
    ]


    @classmethod
    def host(cls):
        return "www.fifteenspatulas.com"
