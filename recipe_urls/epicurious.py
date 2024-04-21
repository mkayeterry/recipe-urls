import re
from recipe_urls._abstract import AbstractScraper


class EpicuriousScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/recipes/food/views/[\w-]+[\w-]")

    @classmethod
    def host(cls):
        return "www.epicurious.com"
