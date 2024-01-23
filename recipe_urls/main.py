from recipe_urls.utils import categorize_url
from recipe_urls.url_scrapers.allrecipes_scraper import AllRecipesScraper

SCRAPER_CLASSES = {
    # 'afghankitchenrecipes': AfghanKitchenRecipesScraper,
    'allrecipes': AllRecipesScraper
    # 'averiecooks': AverieCooksScraper,
    # 'baking-sense': BakingSenseScraper,
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

    return recipe_urls



# Testing 
# url = "https://www.allrecipes1.com"
# urls = get_recipe_urls(url)