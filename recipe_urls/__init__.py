from typing import Any

from recipe_urls.abuelascounter import AbuelasCounterScraper
from recipe_urls.acouplecooks import ACoupleCooksScraper
from recipe_urls.addapinch import AddAPinchScraper
from recipe_urls.afghankitchenrecipes import AfghanKitchenRecipesScraper
from recipe_urls.allrecipes import AllRecipesScraper
from recipe_urls.ambitiouskitchen import AmbitiousKitchenScraper
from recipe_urls.archanaskitchen import ArchanasKitchenScraper
from recipe_urls.averiecooks import AverieCooksScraper
from recipe_urls.bakingmischief import BakingMischiefScraper
from recipe_urls.bakingsense import BakingSenseScraper
from recipe_urls.barefootcontessa import BarefootContessaScraper
from recipe_urls.bbc import BBCScraper
from recipe_urls.bettycrocker import BettyCrockerScraper
from recipe_urls.bigoven import BigOvenScraper
from recipe_urls.bluejeanchef import BlueJeanChefScraper
from recipe_urls.bonappetit import BonAppetitScraper
from recipe_urls.bongeats import BongEatsScraper
from recipe_urls.bowlofdelicious import BowlOfDeliciousScraper
from recipe_urls.budgetbytes import BudgetBytesScraper
from recipe_urls.carlsbadcravings import CarlsbadCravingsScraper
from recipe_urls.castironketo import CastIronKetoScraper
from recipe_urls.cdkitchen import CdKitchenScraper
from recipe_urls.chefsavvy import ChefSavvyScraper
from recipe_urls.closetcooking import ClosetCookingScraper
from recipe_urls.cookieandkate import CookieAndKateScraper
from recipe_urls.copykat import CopyKatScraper
from recipe_urls.countryliving import CountryLivingScraper
from recipe_urls.creativecanning import CreativeCanningScraper
from recipe_urls.davidlebovitz import DavidLebovitzScraper
from recipe_urls.delish import DelishScraper
from recipe_urls.eatingwell import EatingWellScraper
from recipe_urls.food import FoodScraper
from recipe_urls.food52 import Food52Scraper
from recipe_urls.hellofresh import HelloFreshScraper
from recipe_urls.ninjatestkitchen import NinjaTestKitchenScraper
from recipe_urls.nytimes import NyTimesScraper

from recipe_urls._abstract import AbstractScraper
from recipe_urls._utils import get_site_origin

SCRAPERS = {
    AbuelasCounterScraper.host(): AbuelasCounterScraper, 
    ACoupleCooksScraper.host(): ACoupleCooksScraper, 
    AddAPinchScraper.host(): AddAPinchScraper,
    AfghanKitchenRecipesScraper.host(): AfghanKitchenRecipesScraper,
    AllRecipesScraper.host(): AllRecipesScraper, 
    AmbitiousKitchenScraper.host(): AmbitiousKitchenScraper, 
    ArchanasKitchenScraper.host(): ArchanasKitchenScraper, 
    AverieCooksScraper.host(): AverieCooksScraper, 
    BakingMischiefScraper.host(): BakingMischiefScraper, 
    BakingSenseScraper.host(): BakingSenseScraper, 
    BarefootContessaScraper.host(): BarefootContessaScraper, 
    BBCScraper.host(): BBCScraper, 
    BettyCrockerScraper.host(): BettyCrockerScraper, 
    BigOvenScraper.host(): BigOvenScraper, 
    BlueJeanChefScraper.host(): BlueJeanChefScraper, 
    BonAppetitScraper.host(): BonAppetitScraper, 
    BongEatsScraper.host(): BongEatsScraper, 
    BowlOfDeliciousScraper.host(): BowlOfDeliciousScraper, 
    BudgetBytesScraper.host(): BudgetBytesScraper, 
    CarlsbadCravingsScraper.host(): CarlsbadCravingsScraper, 
    CastIronKetoScraper.host(): CastIronKetoScraper, 
    CdKitchenScraper.host(): CdKitchenScraper, 
    ChefSavvyScraper.host(): ChefSavvyScraper, 
    ClosetCookingScraper.host(): ClosetCookingScraper, 
    CookieAndKateScraper.host(): CookieAndKateScraper, 
    CopyKatScraper.host(): CopyKatScraper, 
    CountryLivingScraper.host(): CountryLivingScraper, 
    CreativeCanningScraper.host(): CreativeCanningScraper, 
    DavidLebovitzScraper.host(): DavidLebovitzScraper, 
    DelishScraper.host(): DelishScraper, 
    EatingWellScraper.host(): EatingWellScraper,
    FoodScraper.host(): FoodScraper, 
    Food52Scraper.host(): Food52Scraper, 
    HelloFreshScraper.host(): HelloFreshScraper, 
    NinjaTestKitchenScraper.host(): NinjaTestKitchenScraper, 
    NyTimesScraper.host(): NyTimesScraper
}

def scrape_urls(base_url: str) -> AbstractScraper:
    site_origin = get_site_origin(base_url)
    scraper_class = SCRAPERS.get(site_origin)

    if scraper_class:
        scraper_instance = scraper_class(base_url)
        return scraper_instance.scrape()
    else:
        print(f"[__init__.py] Warning: No scraper found for {site_origin}.")
        return []