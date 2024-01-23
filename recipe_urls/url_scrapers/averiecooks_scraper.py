import re
from ..base_scraper import BaseScraper

class AverieCooksScraper(BaseScraper):
    def scrape(self):
        # Call the base class to get the list of generalized href links
        href_links = super().scrape()

        # Filter href links for recipe-specific ones using site-specific regex
        recipe_links = self.filter_recipe_links(href_links)

        return recipe_links

    def filter_recipe_links(self, href_links):
        print('[averiecooks_scraper.py] Filtering general href links using specififed regex pattern...')

        # Site-specific regex for AverieCooks
        recipe_pattern = re.compile(r'https:\/\/www\.averiecooks\.com\/[\w-]+\/') #TODO: Allowing for more than just recipes

        # Filter href links for recipe-specific ones
        recipe_links = [link for link in href_links if recipe_pattern.search(link)]

        # Raise an error if no recipe links are found
        if not recipe_links:
            raise ValueError("[averiecooks_scraper.py] No recipe links matched the defined pattern for AverieCooks.")

        return recipe_links