import re
from recipe_urls._abstract import AbstractScraper


class SimpleVeganistaScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://simple-veganista\.com/[\w-]+-[\w-]+/")

    @classmethod
    def host(cls):
        return "simple-veganista.com"
