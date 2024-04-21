import re
from recipe_urls._abstract import AbstractScraper


class AddAPinchScraper(AbstractScraper):

    RECIPE_PATTERN = re.compile(r"^https://addapinch\.com/[\w-]+-recipe/$")

    @classmethod
    def host(cls):
        return "addapinch.com"
