import re
from recipe_urls._abstract import AbstractScraper


class JustATasteScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.justataste\.com/[\w-]+-[\w-]+-recipe/")

    @classmethod
    def host(cls):
        return "www.justataste.com"
