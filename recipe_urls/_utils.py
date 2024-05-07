from typing import Optional
from urllib.parse import urlparse
from bs4 import BeautifulSoup

SITE_ORIGINS = [
    "abuelascounter.com",
    "www.acouplecooks.com",
    "addapinch.com",
    "www.afghankitchenrecipes.com",
    "www.allrecipes.com",
    "www.ambitiouskitchen.com",
    "www.archanaskitchen.com",
    "www.averiecooks.com",
    "bakingmischief.com",
    "www.baking-sense.com",
    "barefootcontessa.com",
    "www.bbc.co.uk",
    "www.bettycrocker.com",
    "www.bigoven.com",
    "bluejeanchef.com",
    "www.bonappetit.com",
    "www.bongeats.com",
    "www.bowlofdelicious.com",
    "www.budgetbytes.com",
    "carlsbadcravings.com",
    "www.castironketo.net",
    "www.cdkitchen.com",
    "chefsavvy.com",
    "www.closetcooking.com",
    "cookieandkate.com",
    "copykat.com",
    "www.countryliving.com",
    "creativecanning.com",
    "www.davidlebovitz.com",
    "www.delish.com",
    "domesticate-me.com",
    "downshiftology.com",
    "www.eatingbirdfood.com",
    "www.eatingwell.com",
    "www.eatliverun.com",
    "eatsmarter.com",
    "www.eatwell101.com",
    "eatwhattonight.com",
    "elavegan.com",
    "www.ethanchlebowski.com",
    "www.errenskitchen.com",
    "www.epicurious.com",
    "www.farmhouseonboone.com",
    "www.fifteenspatulas.com",
    "www.finedininglovers.com",
    "fitmencook.com",
    "fitslowcookerqueen.com",
    "www.food.com",
    "food52.com",
    "www.foodandwine.com",
    "www.foodnetwork.com",
    "www.foodrepublic.com",
    "www.forksoverknives.com",
    "forktospoon.com",
    "www.gimmesomeoven.com",
    "goodfooddiscoveries.com",
    "www.goodhousekeeping.com",
    "www.gonnawantseconds.com",
    "www.greatbritishchefs.com",
    "www.halfbakedharvest.com",
    "handletheheat.com",
    "headbangerskitchen.com",
    "heatherchristo.com",
    "www.hellofresh.com",
    "www.hersheyland.com",
    "hostthetoast.com",
    "im-worthy.com",
    "www.indianhealthyrecipes.com",
    "insanelygoodrecipes.com",
    "inspiralized.com",
    "izzycooking.com",
    "www.jamieoliver.com",
    "jimcooksfoodgood.com",
    "joyfoodsunshine.com",
    "www.justataste.com",
    "justbento.com",
    "www.justonecookbook.com",
    "www.kingarthurbaking.com",
    "leanandgreenrecipes.net",
    "lifestyleofafoodie.com",
    "littlespicejar.com",
    "livelytable.com",
    "lovingitvegan.com",
    "ninjatestkitchen.eu",
    "cooking.nytimes.com",
    "ohsheglows.com",
    "www.onceuponachef.com",
    "www.paleorunningmomma.com",
    "www.persnicketyplates.com",
    "www.pickuplimes.com",
    "www.platingpixels.com",
    "rachlmansfield.com",
    "rainbowplantlife.com",
    "reciperunner.com",
    "sallysbakingaddiction.com",
    "simple-veganista.com",
    "www.simplywhisked.com",
    "www.tasteofhome.com",
    "tasty.co",
    "www.wellplated.com",
    "whole30.com",
]


def get_site_origin(
    base_url: Optional[str] = None, html: Optional[str] = None
) -> Optional[str]:
    if base_url:
        if not isinstance(base_url, str):
            raise ValueError("URL format must be of type string.")
        parsed_url = urlparse(base_url)
        hostname, scheme = parsed_url.hostname, parsed_url.scheme
        if not (hostname and scheme):
            raise ValueError("URL must include a valid scheme and hostname.")
        if scheme not in ["https", "http"]:
            raise ValueError("URL scheme must be 'https' or 'http'.")
        if hostname.lower() in SITE_ORIGINS:
            return hostname.lower()
        else:
            raise ValueError("URL not supported.")
    elif html:
        soup = BeautifulSoup(html, "html.parser")
        base_domain = extract_base_domain(soup)
        return base_domain["hostname"]
    else:
        raise ValueError("Either base_url or html must be provided.")


def extract_base_domain(soup: BeautifulSoup) -> dict:
    meta_url = soup.find("meta", property="og:url", content=True)
    if meta_url:
        return parse_url(meta_url["content"])
    canonical_link = soup.find("link", rel="canonical", href=True)
    if canonical_link:
        return parse_url(canonical_link["href"])
    for link in soup.find_all("a", href=True):
        if "http" in link["href"]:
            parsed_link = urlparse(link["href"])
            if parsed_link.netloc.lower() in SITE_ORIGINS:
                return {
                    "scheme": parsed_link.scheme,
                    "hostname": parsed_link.netloc,
                    "path": parsed_link.path,
                }
    raise ValueError(
        "Base URL was not extracted from HTML content. Please provide a base URL."
    )


def parse_url(url: str) -> dict:
    parsed_url = urlparse(url)
    hostname, scheme = parsed_url.hostname, parsed_url.scheme
    if hostname.lower() in SITE_ORIGINS:
        return {"scheme": scheme, "hostname": hostname, "path": parsed_url.path}


def concat_host(
    link: str, base_url: Optional[str], soup: Optional[BeautifulSoup]
) -> str:
    if base_url and "http" in base_url:
        base_parsed = urlparse(base_url)
        return (
            link
            if base_parsed.netloc in link
            else f"{base_parsed.scheme}://{base_parsed.netloc}{link}"
        )
    elif soup:
        base_domain = extract_base_domain(soup)
        if base_domain:
            return (
                link
                if base_domain["hostname"] in link
                else f"{base_domain['scheme']}://{base_domain['hostname']}{link}"
            )
        else:
            return link
