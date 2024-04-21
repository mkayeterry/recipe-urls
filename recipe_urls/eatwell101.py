import re
from recipe_urls._abstract import AbstractScraper


class EatWell101Scraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.eatwell101\.com/[\w-]+-recipe$")

    @classmethod
    def host(cls):
        return "www.eatwell101.com"
