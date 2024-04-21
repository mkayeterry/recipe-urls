import re
from recipe_urls._abstract import AbstractScraper


class TastyScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/recipe/[\w-]+-[\w-]")

    @classmethod
    def host(cls):
        return "tasty.co"
