import re
from recipe_urls._abstract import AbstractScraper


class ElaVeganScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://elavegan\.com/[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "#",
            "about",
            "category",
            "contact",
            "cookbooks",
            "disclosure",
            "feed",
            "ideas",
            "recipes",
            "policy",
        ]
    ]

    @classmethod
    def host(cls):
        return "elavegan.com"
