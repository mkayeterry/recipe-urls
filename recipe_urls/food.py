import re
from recipe_urls._abstract import AbstractScraper


class FoodScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.food\.com/recipe/[\w-]+-[\w-]+-\d")

    @classmethod
    def host(cls):
        return "www.food.com"
