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
    'www.wellplated.com', 
    'whole30.com'
]


def get_site_origin(base_url: Optional[str] = None, html: Optional[str] = None) -> Optional[str]:

    if base_url:

        if not isinstance(base_url, str):
            raise ValueError("URL format must be of type string.")
        
        parsed_url = urlparse(base_url)

        hostname = parsed_url.hostname if not None else parsed_url.netloc
        scheme = parsed_url.scheme

        if not all([scheme, hostname]):
            raise ValueError("URL is not a valid format.")
        
        if scheme not in ['https', 'http']:
            raise ValueError("URL scheme must be 'https' or 'http'.")
        
        normalized_domain = hostname.lower()
        
        if normalized_domain in SITE_ORIGINS:
            return normalized_domain

        else:
            raise ValueError(f"URL not supported.")
    
    elif html:

        if not isinstance(html, str):
            raise ValueError("HTML content must be a string.")
        
        soup = BeautifulSoup(html, "html.parser")
        base_url = extract_base_domain(soup)['hostname']
        return base_url
    
    else:
        raise ValueError("Either base_url or html must be provided.")



def extract_base_domain(soup: BeautifulSoup) -> dict:

    base_domain = {}

    og_url_meta = soup.find("meta", property="og:url", content=True)
    if og_url_meta:
        og_url_parsed = urlparse(og_url_meta['content'])

        hostname = og_url_parsed.hostname if not None else og_url_parsed.netloc
        scheme = og_url_parsed.scheme

        if hostname.lower() in SITE_ORIGINS:
            base_domain.update({
                "scheme": og_url_parsed.scheme,
                "hostname": hostname,
                "path": og_url_parsed.path,
            })

    canonical_url = soup.find("link", {"rel": "canonical", "href": True})
    if canonical_url:
        canonical_url_parsed = urlparse(canonical_url["href"])

        hostname = canonical_url_parsed.hostname if not None else canonical_url_parsed.netloc
        scheme = canonical_url_parsed.scheme

        if hostname.lower() in SITE_ORIGINS:
            base_domain.update({
                "scheme": canonical_url_parsed.scheme,
                "hostname": hostname,
                "path": canonical_url_parsed.path,
            })

    href_links = [urlparse(a["href"]) for a in soup.find_all("a", href=True) if "http" in a["href"]]
    relevant_links = [link for link in href_links if link.netloc.lower() in SITE_ORIGINS]
    if relevant_links:
        hostname_counts = {link: href_links.count(link) for link in relevant_links}
        most_freq_hostname = max(hostname_counts, key=hostname_counts.get)
        
        base_domain.update({
            "scheme": most_freq_hostname.scheme,
            "hostname": most_freq_hostname.hostname if not None else most_freq_hostname.netloc,
            "path": most_freq_hostname.path,
        })

    if base_domain:
        return base_domain
    
    else:
        raise ValueError(f"Base URL was not extracted from HTML content. Please provide a base URL.")



def concat_host(link: str, base_url: str, soup: BeautifulSoup) -> str:

    if base_url and 'http' in base_url:
        base_parsed = urlparse(base_url)
        base_domain = f"{base_parsed.scheme}://{base_parsed.netloc}"
        return link if base_parsed.netloc in link else base_domain + link

    else:
        ext_base_parsed = extract_base_domain(soup)

        if all([ext_base_parsed['scheme'], ext_base_parsed['hostname']]):
            ext_base_domain = f"{ext_base_parsed['scheme']}://{ext_base_parsed['hostname']}" 
            return link if ext_base_parsed['hostname'] in link else ext_base_domain + link

        elif ext_base_parsed['path'] is not None:
            return ext_base_parsed['path'] + link
        
            
