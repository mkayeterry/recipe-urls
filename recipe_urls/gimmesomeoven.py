import re
from recipe_urls._abstract import AbstractScraper


class GimmeSomeOvenScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.gimmesomeoven\.com/[\w-]+-[\w-]+/$")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in ["guide", "how-to", "index", "policy", "work-with-us"]
    ]

    @classmethod
    def host(cls):
        return "www.gimmesomeoven.com"
