import re
from recipe_urls._abstract import AbstractScraper


class PersnicketyPlatesScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.persnicketyplates\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [re.compile(pattern) for pattern in ["contact", "work-with-me"]]

    @classmethod
    def host(cls):
        return "www.persnicketyplates.com"
