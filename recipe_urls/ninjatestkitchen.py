import re
from recipe_urls._abstract import AbstractScraper


class NinjaTestKitchenScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://ninjatestkitchen\.eu/recipe/[\w-]+/$")

    @classmethod
    def host(cls):
        return "ninjatestkitchen.eu"
