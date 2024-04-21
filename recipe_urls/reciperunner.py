import re
from recipe_urls._abstract import AbstractScraper


class RecipeRunnerScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://reciperunner\.com/(?![\w-]*\d)[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "exercise",
            "ideas",
            "meals",
            "review",
            "safe",
            "tips",
            "workout",
        ]
    ]

    @classmethod
    def host(cls):
        return "reciperunner.com"
