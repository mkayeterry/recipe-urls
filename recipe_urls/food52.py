import re
from recipe_urls._abstract import AbstractScraper


class Food52Scraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/recipes/\d+-[\w-]+-[\w-]")

    @classmethod
    def host(cls):
        return "food52.com"
