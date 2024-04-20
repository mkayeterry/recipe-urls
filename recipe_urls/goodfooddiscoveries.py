import re
from recipe_urls._abstract import AbstractScraper


class GoodFoodDiscoveriesScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://goodfooddiscoveries\.com/[\w-]+-[\w-]+/$")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in ["index", "disclosure", "policy", "preferences", "terms"]
    ]

    @classmethod
    def host(cls):
        return "goodfooddiscoveries.com"
