import re
from recipe_urls._abstract import AbstractScraper


class FoodAndWineScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https://www\.foodandwine\.com/[\w/-]+-\d+")
    UNWANTED_PATTERNS = [
        re.compile(pattern) 
        for pattern in [
            "best", 
            "career", 
            "cook", 
            "deal", 
            "guide", 
            "grilling", 
            "how-to",
            "news",  
            "small",  
            "snacks", 
            "tastemaker", 
            "term", 
            "trend", 
            "viral", 
            "winner"
        ]
    ]

    @classmethod
    def host(cls):
        return "www.foodandwine.com"
