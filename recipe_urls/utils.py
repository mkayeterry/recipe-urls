from recipe_urls.url_scrapers.afghankitchenrecipes_scraper import AfghanKitchenRecipesScraper
from recipe_urls.url_scrapers.allrecipes_scraper import AllRecipesScraper
from recipe_urls.url_scrapers.averiecooks_scraper import AverieCooksScraper
from recipe_urls.url_scrapers.bakingsense_scraper import BakingSenseScraper
from recipe_urls.url_scrapers.bongeats_scraper import BongEatsScraper
from recipe_urls.url_scrapers.food52_scraper import Food52Scraper
from recipe_urls.url_scrapers.food_scraper import FoodScraper
from recipe_urls.url_scrapers.hellofresh_scraper import HelloFreshScraper
from recipe_urls.url_scrapers.nytimes_scraper import NyTimesScraper

def categorize_url(base_url):
    site_classes = {
        'afghankitchenrecipes': 'AfghanKitchenRecipesScraper',
        'allrecipes': 'AllRecipesScraper',
        'averiecooks': 'AverieCooksScraper',
        'baking-sense': 'BakingSenseScraper',
        'bongeats': 'BongEatsScraper',
        'food52': 'Food52Scraper',
        'food': 'FoodScraper',
        'hellofresh': 'HelloFreshScraper',
        'nytimes': 'NyTimesScraper'
    }

    for site_key, class_name in site_classes.items():
        if site_key in base_url:
            return class_name

    return None  # Return None if no matching class is found