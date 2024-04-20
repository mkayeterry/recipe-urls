import re
from recipe_urls._abstract import AbstractScraper


class ForksOverKnivesScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/recipes/[\w-]+/[\w-]+/")
    UNWANTED_PATTERNS = [re.compile(pattern) for pattern in ["collections"]]

    @classmethod
    def host(cls):
        return "www.forksoverknives.com"
