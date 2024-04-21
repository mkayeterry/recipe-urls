import re
from recipe_urls._abstract import AbstractScraper


class BongEatsScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/recipe/([\w-]+)")

    @classmethod
    def host(cls):
        return "www.bongeats.com"
