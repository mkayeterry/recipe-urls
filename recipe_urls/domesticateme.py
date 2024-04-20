from typing import List
import re
from recipe_urls._abstract import AbstractScraper

class DomesticateMeScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r'https://domesticate-me\.com/[\w-]+/')
    UNWANTED_PATTERNS = [re.compile(pattern) for pattern in ["category", "contact", "library", "press", "policy", "recipes", "serena", "shop", "work-with-me",]]

    @classmethod
    def host(cls):
        return "domesticate-me.com"

