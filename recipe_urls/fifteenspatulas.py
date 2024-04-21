import re
from recipe_urls._abstract import AbstractScraper


class FifteenSpatulasScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.fifteenspatulas\.com/[\w-]+/$")

    @classmethod
    def host(cls):
        return "www.fifteenspatulas.com"
