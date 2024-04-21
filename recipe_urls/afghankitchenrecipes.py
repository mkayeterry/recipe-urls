import re
from recipe_urls._abstract import AbstractScraper


class AfghanKitchenRecipesScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(
        r"https?://www\.afghankitchenrecipes\.com/recipe/[\w-]+/"
    )

    @classmethod
    def host(cls):
        return "www.afghankitchenrecipes.com"
