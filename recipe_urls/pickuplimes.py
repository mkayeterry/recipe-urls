import re
from recipe_urls._abstract import AbstractScraper


class PickUpLimesScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/recipe/[\w/-]+\d+$")

    @classmethod
    def host(cls):
        return "www.pickuplimes.com"
