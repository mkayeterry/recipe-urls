import re
from recipe_urls._abstract import AbstractScraper


class JamieOliverScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/recipes/[\w-]+-recipes/[\w-]+-[\w-]+/")

    @classmethod
    def host(cls):
        return "www.jamieoliver.com"
