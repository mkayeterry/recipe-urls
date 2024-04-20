import re
from recipe_urls._abstract import AbstractScraper


class IndianHealthyRecipesScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(
        r"https://www\.indianhealthyrecipes\.com/[\w-]+-[\w-]+/"
    )
    UNWANTED_PATTERNS = [re.compile(pattern) for pattern in ["_", "-recipes"]]

    @classmethod
    def host(cls):
        return "www.indianhealthyrecipes.com"
