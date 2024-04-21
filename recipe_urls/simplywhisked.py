import re
from recipe_urls._abstract import AbstractScraper


class SimplyWhiskedScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(
        r"https://www\.simplywhisked\.com/(?![\w-]*\d)[\w-]+-[\w-]+/"
    )
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "about",
            "hidden",
            "index",
            "kitchen",
            "resource",
            "policy",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.simplywhisked.com"
