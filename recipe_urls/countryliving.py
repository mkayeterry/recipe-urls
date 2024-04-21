import re
from recipe_urls._abstract import AbstractScraper


class CountryLivingScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/food-drinks/a\d+/[\w-]+-[\w-]+-recipe/$")

    @classmethod
    def host(cls):
        return "www.countryliving.com"
