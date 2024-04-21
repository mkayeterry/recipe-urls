import re
from recipe_urls._abstract import AbstractScraper


class InsanelyGoodRecipesScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://insanelygoodrecipes\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern) for pattern in ["contact", "search", "-recipes"]
    ]

    @classmethod
    def host(cls):
        return "insanelygoodrecipes.com"
