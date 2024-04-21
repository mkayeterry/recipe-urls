import re
from recipe_urls._abstract import AbstractScraper


class GreatBritishChefsScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(
        r"https://www\.greatbritishchefs\.com/recipes/[\w-]+-[\w-]"
    )

    @classmethod
    def host(cls):
        return "www.greatbritishchefs.com"
