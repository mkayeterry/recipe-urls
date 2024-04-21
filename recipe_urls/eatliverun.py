import re
from recipe_urls._abstract import AbstractScraper


class EatLiveRunScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"https?://www\.eatliverun\.com/[\w-]+-[\w-]+/")
    UNWANTED_PATTERNS = [
        re.compile(pattern)
        for pattern in [
            "#",
            "about",
            "author",
            "baby",
            "birth",
            "category",
            "contact",
            "content",
            "cookbooks",
            "facebook",
            "google",
            "homeschool",
            "page",
            "pinterest",
            "policy",
            "recipes",
            "recommend",
            "twitter",
            "work-with-us",
        ]
    ]

    @classmethod
    def host(cls):
        return "www.eatliverun.com"
