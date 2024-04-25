import re
from recipe_urls._abstract import AbstractScraper


class CdKitchenScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(
        r"https://www\.cdkitchen\.com/recipes/[\w-]+/\d+/[\w-]+\.shtml"
    )

    @classmethod
    def host(cls):
        return "www.cdkitchen.com"
