import re
from recipe_urls._abstract import AbstractScraper


class JustBentoScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/handbook/[\w-]+/[\w-]+-[\w-]+")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "bento-basics",
        ]
    ]

    @classmethod
    def host(cls):
        return "justbento.com"
