from typing import List
from recipe_urls.utils import categorize_url
from recipe_urls.url_scrapers.afghankitchenrecipes_scraper import AfghanKitchenRecipesScraper
from recipe_urls.url_scrapers.allrecipes_scraper import AllRecipesScraper
# from recipe_urls.url_scrapers.averiecooks_scraper import AverieCooksScraper #TODO: fix regex
from recipe_urls.url_scrapers.bakingsense_scraper import BakingSenseScraper
from recipe_urls.url_scrapers.bongeats_scraper import BongEatsScraper
from recipe_urls.url_scrapers.food_scraper import FoodScraper
from recipe_urls.url_scrapers.food52_scraper import Food52Scraper
# from recipe_urls.url_scrapers.hellofresh_scraper import HelloFreshScraper
# from recipe_urls.url_scrapers.nytimes_scraper import NyTimesScraper

SCRAPER_CLASSES = {
    'afghankitchenrecipes': AfghanKitchenRecipesScraper, 
    'allrecipes': AllRecipesScraper, 
    # 'averiecooks': AverieCooksScraper, #TODO: fix regex
    'baking-sense': BakingSenseScraper, 
    'bongeats': BongEatsScraper, 
    'food': FoodScraper, 
    'food52': Food52Scraper
    # 'hellofresh': HelloFreshScraper,
    # 'nytimes': NyTimesScraper
}

def get_recipe_urls(base_url: str) -> List[str]:
    """
    Extracts recipe information from a list of base URLs using specific scraper classes.

    Args:
    - base_url (str): A single base URL to extract recipes from.

    Returns:
    - List[str]: A list of recipe URLs.
    """

    # Categorize the URL to determine the appropriate scraper class
    site_origin = categorize_url(base_url)

    # Get the scraper class from the dictionary
    scraper_class = SCRAPER_CLASSES[site_origin]
    print(f"[main.py] {base_url} successfully matched to {scraper_class}.")
    
    try:
        # Create an instance
        scraper_instance = scraper_class(base_url)
       
        # Call the specified scrape method
        recipe_urls = scraper_instance.scrape()
        print(f"[main.py] {len(recipe_urls)} recipe URLs scraped from {base_url}.")

    except KeyError as e:
        print(f"[main.py] Error: Scraper instance was unsuccessful for URL '{base_url}'.")

    return recipe_urls



# Testing 
urls = ['https://food52.com']
compiled_urls = []

for url in urls:
    recipes = get_recipe_urls(url)
    compiled_urls.extend(recipes)


'https://www.baking-sense.com'
'https://www.allrecipes.com'
'http://www.afghankitchenrecipes.com'
'https://www.bongeats.com'
'https://www.food.com'
'https://food52.com'