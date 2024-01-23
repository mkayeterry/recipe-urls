from recipe_urls.utils import categorize_url
from recipe_urls.url_scrapers.afghankitchenrecipes_scraper import AfghanKitchenRecipesScraper
from recipe_urls.url_scrapers.allrecipes_scraper import AllRecipesScraper
# from recipe_urls.url_scrapers.averiecooks_scraper import AverieCooksScraper #TODO: fix regex
from recipe_urls.url_scrapers.bakingsense_scraper import BakingSenseScraper
# from recipe_urls.url_scrapers.bongeats_scraper import BongEatsScraper
# from recipe_urls.url_scrapers.food52_scraper import Food52Scraper
# from recipe_urls.url_scrapers.food_scraper import FoodScraper
# from recipe_urls.url_scrapers.hellofresh_scraper import HelloFreshScraper
# from recipe_urls.url_scrapers.nytimes_scraper import NyTimesScraper

SCRAPER_CLASSES = {
    'afghankitchenrecipes': AfghanKitchenRecipesScraper, 
    'allrecipes': AllRecipesScraper, 
    # 'averiecooks': AverieCooksScraper, #TODO: fix regex
    'baking-sense': BakingSenseScraper
    # 'bongeats': BongEatsScraper,
    # 'food52': Food52Scraper,
    # 'food': FoodScraper,
    # 'hellofresh': HelloFreshScraper,
    # 'nytimes': NyTimesScraper
}

def get_recipe_urls(base_urls):
    """
    Extracts recipe information from a list of base URLs using specific scraper classes.

    Args:
    - base_urls (str or list): A single base URL or a list of base URLs to extract recipes from.

    Returns:
    - list: A list of recipe URLs
    """
    # Ensure base_urls is a list for uniform processing
    if not isinstance(base_urls, list):
        base_urls = [base_urls]

    # Initialize an empty list to store recipe URLs
    compiled_recipe_urls = []

    # Iterate through each base URL
    for base_url in base_urls:
        # Categorize the URL to determine the appropriate scraper class
        site_origin = categorize_url(base_url)
        
        try:
            # Get the scraper class from the dictionary
            scraper_class = SCRAPER_CLASSES[site_origin]
            print(f"[main.py] {base_url} successfully matched to {scraper_class}.")
            
            # Create an instance and call the scrape method
            scraper_instance = scraper_class(base_url)
            
            # Append the recipe URLs to the list
            recipe_urls = scraper_instance.scrape()
            print(f"[main.py] {len(recipe_urls)} recipe URLs scraped from {base_url}.")
            compiled_recipe_urls.extend(recipe_urls)

        except KeyError:
            print(f"[main.py] Error: Scraper class not found for URL '{base_url}'.")

    return compiled_recipe_urls



# Testing 
# url = ['https://www.baking-sense.com', 'https://www.allrecipes.com', 'http://www.afghankitchenrecipes.com']
# urls = get_recipe_urls(url)


