import re
from recipe_urls._abstract import AbstractScraper


class RainbowPlantLifeScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(
        r"https://rainbowplantlife\.com/(?![\w-]*\d)[\w-]+-[\w-]+/"
    )
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "accessibility",
            "add",
            "alternatives",
            "daily",
            "essential",
            "equipment",
            "guide",
            "grocery",
            "policy",
            "recipes",
            "sources",
            "stories",
            "tips",
            "work",
        ]
    ]

    @classmethod
    def host(cls):
        return "rainbowplantlife.com"
