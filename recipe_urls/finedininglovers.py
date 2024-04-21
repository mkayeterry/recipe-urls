import re
from recipe_urls._abstract import AbstractScraper


class FineDiningLoversScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/recipes/[\w-]+[\w-]")

    @classmethod
    def host(cls):
        return "www.finedininglovers.com"
