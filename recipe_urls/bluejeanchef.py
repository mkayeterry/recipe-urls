import re
from recipe_urls._abstract import AbstractScraper


class BlueJeanChefScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://bluejeanchef\.com/recipes/[\w-]+-[\w-]+/")

    @classmethod
    def host(cls):
        return "bluejeanchef.com"
