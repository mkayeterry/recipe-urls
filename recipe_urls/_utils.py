from typing import Optional
from urllib.parse import urlparse
from bs4 import BeautifulSoup

SITE_ORIGINS = [
    'abuelascounter.com', 
    'www.acouplecooks.com', 
    'addapinch.com', 
    'www.afghankitchenrecipes.com', 
    'www.allrecipes.com', 
    'www.ambitiouskitchen.com', 
    'www.archanaskitchen.com', 
    'www.averiecooks.com',
    'bakingmischief.com',
    'www.baking-sense.com',
    'barefootcontessa.com',
    'www.bbc.co.uk',  
    'www.bettycrocker.com', 
    'www.bigoven.com', 
    'bluejeanchef.com', 
    'www.bonappetit.com', 
    'www.bongeats.com',
    'www.bowlofdelicious.com', 
    'www.budgetbytes.com', 
    'carlsbadcravings.com', 
    'www.castironketo.net', 
    'www.cdkitchen.com', 
    'chefsavvy.com', 
    'www.closetcooking.com', 
    'cookieandkate.com',
    'copykat.com', 
    'www.countryliving.com',
    'creativecanning.com',  
    'www.davidlebovitz.com', 
    'www.delish.com', 
    'domesticate-me.com', 
    'downshiftology.com', 
    'www.eatingbirdfood.com', 
    'www.eatingwell.com', 
    'www.eatliverun.com', 
    'eatsmarter.com', 
    'www.eatwell101.com', 
    'eatwhattonight.com', 
    'elavegan.com', 
    'www.ethanchlebowski.com', 
    'www.errenskitchen.com', 
    'www.epicurious.com', 
    'www.farmhouseonboone.com', 
    'www.fifteenspatulas.com', 
    'www.finedininglovers.com', 
    'fitmencook.com', 
    'fitslowcookerqueen.com', 
    'www.food.com',
    'food52.com',
    'www.foodandwine.com', 
    'www.foodnetwork.com', 
    'www.foodrepublic.com', 
    'www.forksoverknives.com', 
    'forktospoon.com', 
    'www.gimmesomeoven.com', 
    'goodfooddiscoveries.com', 
    'www.goodhousekeeping.com', 
    'www.gonnawantseconds.com',
    'www.greatbritishchefs.com', 
    'www.halfbakedharvest.com', 
    'handletheheat.com', 
    'headbangerskitchen.com', 
    'heatherchristo.com',  
    'www.hellofresh.com',
    'www.hersheyland.com',
    'hostthetoast.com', 
    'im-worthy.com', 
    'www.indianhealthyrecipes.com', 
    'insanelygoodrecipes.com', 
    'inspiralized.com', 
    'izzycooking.com', 
    'www.jamieoliver.com',
    'jimcooksfoodgood.com', 
    'joyfoodsunshine.com',  
    'www.justataste.com', 
    'justbento.com', 
    'www.justonecookbook.com', 
    'www.kingarthurbaking.com', 
    'leanandgreenrecipes.net',
    'lifestyleofafoodie.com',  
    'littlespicejar.com', 
    'livelytable.com', 
    'lovingitvegan.com', 
    'ninjatestkitchen.eu', 
    'cooking.nytimes.com', 
    'ohsheglows.com', 
    'www.onceuponachef.com', 
    'www.paleorunningmomma.com', 
    'www.persnicketyplates.com', 
    'www.pickuplimes.com',
    'www.platingpixels.com', 
    'rachlmansfield.com',
    'rainbowplantlife.com', 
    'reciperunner.com', 
    'sallysbakingaddiction.com', 
    'simple-veganista.com', 
    'www.simplywhisked.com', 
    'www.tasteofhome.com', 
    'tasty.co', 
    'www.wellplated.com'
]

def extract_base_domain(domain: str) -> str:

    domain = domain.lower()  # Ensure case consistency
    return domain

def get_site_origin(base_url: Optional[str] = None, html: Optional[str] = None) -> Optional[str]:

    if base_url:

        if not isinstance(base_url, str):
            raise ValueError("URL format must be of type string.")
        
        parsed_url = urlparse(base_url)

        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError("URL is not a valid format")
        
        if parsed_url.scheme not in ['https', 'http']:
            raise ValueError("URL scheme must be 'https' or 'http'.")
        
        normalized_domain = extract_base_domain(parsed_url.hostname)
        
        if normalized_domain in SITE_ORIGINS:
            return normalized_domain

        else:
            raise ValueError(f"URL not supported.")
    
    elif html:

        if not isinstance(html, str):
            raise ValueError("HTML content must be a string")
        
        soup = BeautifulSoup(html, "html.parser")
        href_links = [urlparse(a["href"]).hostname for a in soup.find_all("a", href=True) if "http" in a["href"]]
        relevant_links = [link for link in href_links if link in SITE_ORIGINS]
        
        if relevant_links:
            # Returns the most frequently occurring domain that matches the known origins
            return max(set(relevant_links), key=relevant_links.count)

        else:
            raise ValueError("Site origin not found in HTML content.")
    
    else:
        raise ValueError("Either base_url or html must be provided.")

