import re
from recipe_urls._abstract import AbstractScraper


class OnceUponAChefScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(
        r"https://www\.onceuponachef\.com/recipes/[\w/-]+\.html"
    )

    @classmethod
    def host(cls):
        return "www.onceuponachef.com"
