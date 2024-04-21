import re
from recipe_urls._abstract import AbstractScraper


class DelishScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/cooking/recipe-ideas/a\d+/[\w-]+-[\w-]+-recipe/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "#",
            "category",
            "policy",
            "statement",
            "terms",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.delish.com"
