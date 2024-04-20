import re
from recipe_urls._abstract import AbstractScraper


class NyTimesScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/recipes/\d+-[\w-]+-[\w-]")

    @classmethod
    def host(cls):
        return "cooking.nytimes.com"
