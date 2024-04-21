import re
from recipe_urls._abstract import AbstractScraper


class BBCScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/food/recipes/[\w-]+_[\w-]+_(\d+)")

    @classmethod
    def host(cls):
        return "www.bbc.co.uk"
