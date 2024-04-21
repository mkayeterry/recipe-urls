import re
from recipe_urls._abstract import AbstractScraper


class BakingSenseScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(
        r"https://www\.baking-sense\.com/\d+/\d+/\d+/+[\w-]+-[\w-]+/"
    )
    UNWANTED_PATTERNS = [
        re.compile(pattern) for pattern in ["ingredients", "how", "technique"]
    ]

    @classmethod
    def host(cls):
        return "www.baking-sense.com"
