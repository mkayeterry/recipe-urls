import re
from recipe_urls._abstract import AbstractScraper


class BarefootContessaScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://barefootcontessa\.com/recipes/[\w-]+-[\w-]")

    @classmethod
    def host(cls):
        return "barefootcontessa.com"
