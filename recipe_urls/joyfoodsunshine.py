import re
from recipe_urls._abstract import AbstractScraper


class JoyFoodSunshineScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://joyfoodsunshine\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "how-to",
            "updates",
            "recipe-index",
            "policy",
            "work-with-me",
        ]
    ]

    @classmethod
    def host(cls):
        return "joyfoodsunshine.com"
