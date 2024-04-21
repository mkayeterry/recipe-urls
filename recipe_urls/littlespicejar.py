import re
from recipe_urls._abstract import AbstractScraper


class LittleSpiceJarScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://littlespicejar\.com/[\w/-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "about",
            "category",
            "faq",
            "index",
            "page",
            "policy",
            "resources",
        ]
    ]

    @classmethod
    def host(cls):
        return "littlespicejar.com"
