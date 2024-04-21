import re
from recipe_urls._abstract import AbstractScraper


class FoodRepublicScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/\d+/[\w-]+[\w-]+recipe/")

    @classmethod
    def host(cls):
        return "www.foodrepublic.com"
