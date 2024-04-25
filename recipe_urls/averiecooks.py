import re
from recipe_urls._abstract import AbstractScraper


class AverieCooksScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.averiecooks\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern) 
        for pattern in [
            "gift", 
            "index", 
            "interview", 
            "updates", 
            "policy", 
            "no-ai", 
            "web-stories", 
            "work-with-me"
        ]
    ]

    @classmethod
    def host(cls):
        return "www.averiecooks.com"
