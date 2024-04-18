from typing import Optional
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from collections import Counter


def get_site_origin(base_url: str | None = None, html: str | None = None) -> Optional[str]:
    """
    Get the origin of a website based on either a provided base URL or HTML content, prioritiziing use of base URL.

    Args:
        base_url (str | None): The base URL of the website. Defaults to None.
        html (str | None): The HTML content of the website. Defaults to None.

    Returns:
        Optional[str]: The origin of the website if found, otherwise None.

    Raises:
        ValueError: If the provided URL format is not supported or if the site origin is not found in the HTML.
    """
    site_origins = [
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
        'tasty.co'
    ]

    # Prioritizes base_url
    if base_url:

        if not isinstance(base_url, str):
            raise ValueError(f"URL format '{type(base_url)}' is not supported.")

        # If https:// is not specified
        for site_origin in site_origins:
            if site_origin == base_url:
                return site_origin

        # If https:// is specified
        parsed_url = urlparse(base_url).hostname
        for site_origin in site_origins:
            if site_origin == parsed_url:
                return site_origin

        raise ValueError(f"URL '{base_url}' is not supported.")

    # If base_url is not provided  
    if html:

        if not isinstance(html, str):
            raise ValueError(f"HTML format '{type(html)}' is not supported.")
        
        soup = BeautifulSoup(html, "html.parser")
        href_links = [urlparse(a["href"]).hostname for a in soup.find_all("a", href=True) if "https" in a["href"]]
        relevent_links = [link for link in href_links if link in site_origins]

        if relevent_links:
            # Count occurrences of site_origins and return highest count
            site_origin_counter = Counter(relevent_links)
            most_common_site_origin = site_origin_counter.most_common(1)
            most_common_site_origin = most_common_site_origin[0][0]

            return most_common_site_origin

        else:
            raise ValueError(f"Site origin not found in HTML.")

    else:
        raise ValueError("Either base_url or html must be provided.")



