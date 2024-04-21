import re
from recipe_urls._abstract import AbstractScraper


class HelloFreshScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.hellofresh\.com/recipes/[\d\w-]+-\w{24}")

    @classmethod
    def host(cls):
        return "www.hellofresh.com"
