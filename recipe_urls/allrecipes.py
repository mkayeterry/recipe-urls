import re
from recipe_urls._abstract import AbstractScraper


class AllRecipesScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(
        r"https://www\.allrecipes\.com/recipe/\d+/[\w-]+-[\w-]+/"
    )

    @classmethod
    def host(cls):
        return "www.allrecipes.com"
