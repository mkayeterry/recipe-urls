import re
from recipe_urls._abstract import AbstractScraper


class CastIronKetoScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.castironketo\.net/blog/[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "calculator", 
            "category",
            "can",
            "options",
            "recipes",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.castironketo.net"
