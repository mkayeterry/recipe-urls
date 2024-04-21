import re
from recipe_urls._abstract import AbstractScraper


class BakingMischiefScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://bakingmischief\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [re.compile(pattern) for pattern in ["baking-mischief", "how"]]

    @classmethod
    def host(cls):
        return "bakingmischief.com"
