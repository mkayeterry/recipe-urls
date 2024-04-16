from recipe_urls import scrape_urls

links = scrape_urls('https://www.simplywhisked.com')
print(links)

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
    "https://www.epicurious.com", 
    "https://www.errenskitchen.com", 
    "https://www.ethanchlebowski.com/cooking-techniques-recipes", 
    "https://www.farmhouseonboone.com", 
    "https://www.fifteenspatulas.com", 
    "https://www.finedininglovers.com/recipes", 
    "https://fitmencook.com/recipes/", 
    "https://fitslowcookerqueen.com", 
    "https://www.food.com", 
    "https://food52.com", 
    "https://www.foodandwine.com/recipes", 
    "https://www.foodnetwork.com/recipes", # 403 error
    "https://www.foodrepublic.com/category/recipes/", 
    "https://www.forksoverknives.com", 
    "https://forktospoon.com/category/recipes/", 
    "https://www.gimmesomeoven.com", 
    "https://www.gonnawantseconds.com", 
    "https://goodfooddiscoveries.com",
    "https://www.goodhousekeeping.com/food-recipes/", 
    "https://www.greatbritishchefs.com", 
    "https://www.halfbakedharvest.com",
    "https://handletheheat.com",  
    "https://headbangerskitchen.com", 
    "https://heatherchristo.com",  
    "https://www.hellofresh.com/recipes", 
    "https://www.hersheyland.com/recipes",
    "https://hostthetoast.com/recipes/", 
    "https://im-worthy.com", 
    "https://www.indianhealthyrecipes.com",
    "https://insanelygoodrecipes.com",  
    "https://inspiralized.com", 
    "https://izzycooking.com", 
    "https://www.jamieoliver.com", 
    "https://jimcooksfoodgood.com", 
    "https://joyfoodsunshine.com/recipe-index/", 
    "https://www.justataste.com", 
    "https://justbento.com/recipes/all", 
    "https://www.justonecookbook.com", 
    "https://www.kingarthurbaking.com", 
    "https://leanandgreenrecipes.net", 
    "https://lifestyleofafoodie.com", 
    "https://littlespicejar.com", 
    "https://livelytable.com", 
    "https://lovingitvegan.com", 
    "https://ninjatestkitchen.eu", 
    "https://cooking.nytimes.com", 
    "https://ohsheglows.com", 
    "https://www.onceuponachef.com", 
    "https://www.paleorunningmomma.com", 
    "https://www.persnicketyplates.com", 
    "https://pickuplimes.com", 
    "https://www.platingpixels.com", 
    "https://rachlmansfield.com", 
    "https://rainbowplantlife.com", 
    "https://reciperunner.com", 
    "https://sallysbakingaddiction.com", 
    "https://simple-veganista.com", 
    "https://www.simplywhisked.com"
]

compiled_recipe_links = []

for base_url in base_urls:
    try:
        scrape = scrape_urls(base_url)
        compiled_recipe_links.extend(scrape)
    except Exception as e:
        print(e)

print(len(compiled_recipe_links))


###############################################################################################
# BASE_SCRAPER

import httpx
from bs4 import BeautifulSoup
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
}

base_url = 'https://www.simplyquinoa.com'

try:
    response = httpx.get(url=base_url, headers=HEADERS)
    if response.status_code == 403:
        raise httpx.HTTPError(f"Access to {base_url} is forbidden (403).")
    html = response.content
    soup = BeautifulSoup(html, "html.parser")

except httpx.HTTPError as e:
    raise httpx.HTTPError(f"HTTP error for {base_url}. {e}") from e

except Exception as e:
    raise RuntimeError(f"Unexpected error accessing {base_url}. {e}") from e

href_links = [a["href"] for a in soup.find_all("a", href=True)]

recipe_pattern = re.compile(r'/recipe/[\w/-]+\d+$')

# Use a set to deduplicate the links while filtering href links for recipe-specific ones
unique_links_set = set(link for link in href_links if recipe_pattern.search(link))
print(unique_links_set)

###############################################################################################
