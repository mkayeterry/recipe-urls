import re
from recipe_urls._abstract import AbstractScraper


class EthanChlebowskiScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/cooking-techniques-recipes/[\w-]+-[\w-]")
    UNWANTED_PATTERNS = [re.compile(pattern) for pattern in ["category", "meal", "tag"]]

    @classmethod
    def host(cls):
        return "www.ethanchlebowski.com"
