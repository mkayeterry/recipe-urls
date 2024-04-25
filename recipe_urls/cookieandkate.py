import re
from recipe_urls._abstract import AbstractScraper


class CookieAndKateScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://cookieandkate\.com/[\w-]+-[\w-]+recipe/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "recipes",
            "#"
        ]
    ]

    @classmethod
    def host(cls):
        return "cookieandkate.com"
