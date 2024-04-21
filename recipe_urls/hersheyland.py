import re
from recipe_urls._abstract import AbstractScraper


class HersheylandScraper(AbstractScraper):
    RECIPE_PATTERN = re.compile(r"/recipes/[\w-]+-[\w-]+\.html")
    CUSTOM_HREF = ("a", {"class": re.compile("item col")})

    @classmethod
    def host(cls):
        return "www.hersheyland.com"
