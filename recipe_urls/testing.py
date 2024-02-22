from recipe_urls import scrape_urls
import warnings

links = scrape_urls('https://www.eatwell101.com')

base_urls = [
    "https://abuelascounter.com", 
    "https://www.acouplecooks.com", 
    "https://addapinch.com", 
    "http://www.afghankitchenrecipes.com", 
    "https://www.allrecipes.com", 
    "https://www.ambitiouskitchen.com", 
    "https://www.archanaskitchen.com", 
    "https://www.averiecooks.com", 
    "https://bakingmischief.com", 
    "https://www.baking-sense.com", 
    "https://barefootcontessa.com", 
    "https://www.bbc.co.uk/food", 
    "https://www.bettycrocker.com", 
    "https://www.bigoven.com", 
    "https://bluejeanchef.com", 
    "https://www.bonappetit.com", 
    "https://www.bongeats.com", 
    "https://www.bowlofdelicious.com", 
    "https://www.budgetbytes.com",
    "https://carlsbadcravings.com",  
    "https://www.castironketo.net", 
    "https://www.cdkitchen.com", 
    "https://chefsavvy.com",
    "https://www.closetcooking.com/top-recipes/",  
    "https://cookieandkate.com/recipes/", 
    "https://copykat.com/100-favorite-copycat-recipes/", 
    "https://www.countryliving.com/food-drinks/", 
    "https://creativecanning.com", 
    "https://www.davidlebovitz.com/blog/", 
    "https://www.delish.com/cooking/recipe-ideas/", 
    "https://domesticate-me.com/category/recipes/", 
    "https://downshiftology.com", 
    "https://www.eatingbirdfood.com", 
    "https://www.eatingwell.com/recipes/", 
    "https://www.eatliverun.com/recipes/", 
    "https://www.eatwell101.com", 
    "https://eatsmarter.com", 
    "https://www.food.com", 
    "https://food52.com", 
    "https://www.hellofresh.com/recipes", 
    "https://ninjatestkitchen.eu", 
    "https://cooking.nytimes.com"
]

compiled_recipe_links = []

for base_url in base_urls:
    try:
        scrape = scrape_urls(base_url)
        compiled_recipe_links.extend(scrape)
    except:
        warnings.warn(f'{base_url} was unsuccessful.')
        continue

print(len(compiled_recipe_links))

