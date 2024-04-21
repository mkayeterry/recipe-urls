import re
from recipe_urls._abstract import AbstractScraper


class KingArthurBakingScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/recipes/[\w-]+-[\w-]+-recipe")

    @classmethod
    def host(cls):
        return "www.kingarthurbaking.com"
