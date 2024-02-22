from recipe_urls import scrape_urls

links = scrape_urls('https://www.ethanchlebowski.com/cooking-techniques-recipes')

# import re

# urls = [
#     "https://www.ethanchlebowski.com/cooking-techniques-recipes/thai-sausage-stir-fry-amp-freezer-ground-sausage-meal-prep",
#     "https://www.ethanchlebowski.com/cooking-techniques-recipes/creamy-mac-amp-cheese-template-w-any-cheeses",
#     "https://www.ethanchlebowski.com/cooking-techniques-recipes/steak-amp-corn-salsa-tostada"
# ]

# recipe_pattern = re.compile(r'https://www\.ethanchlebowski\.com/.+/.+/.+/$')

# recipe_urls = [url for url in urls if recipe_pattern.match(url)]
# print(recipe_urls)



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
    "https://eatwhattonight.com", 
    "https://elavegan.com", 
    "https://www.ethanchlebowski.com/cooking-techniques-recipes", 
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
    except Exception as e:
        print(f'There was an error processing {base_url}. {e}')
        continue

print(len(compiled_recipe_links))

