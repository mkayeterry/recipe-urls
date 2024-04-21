import re
from recipe_urls._abstract import AbstractScraper


class JustOneCookbookScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.justonecookbook\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "accessibility",
            "conditions",
            "gifts",
            "guide",
            "how-to",
            "index",
            "ingredient",
            "japanese",
            "login",
            "membership",
            "permissions",
            "policy",
            "recipes",
            "start",
            "stores",
            "tips",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.justonecookbook.com"
