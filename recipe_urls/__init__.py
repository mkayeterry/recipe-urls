from typing import Optional
import httpx

from recipe_urls._abstract import AbstractScraper
from recipe_urls._utils import get_site_origin

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
from recipe_urls.domesticateme import DomesticateMeScraper
from recipe_urls.downshiftology import DownshiftologyScraper
from recipe_urls.eatingbirdfood import EatingBirdFoodScraper
from recipe_urls.eatingwell import EatingWellScraper
from recipe_urls.eatliverun import EatLiveRunScraper
from recipe_urls.eatsmarter import EatSmarterScraper
from recipe_urls.eatwell101 import EatWell101Scraper
from recipe_urls.eatwhattonight import EatWhatTonightScraper
from recipe_urls.elavegan import ElaVeganScraper
from recipe_urls.epicurious import EpicuriousScraper
from recipe_urls.errenskitchen import ErrensKitchenScraper
from recipe_urls.ethanchlebowski import EthanChlebowskiScraper
from recipe_urls.farmhouseonboone import FarmhouseOnBooneScraper
from recipe_urls.fifteenspatulas import FifteenSpatulasScraper
from recipe_urls.finedininglovers import FineDiningLoversScraper
from recipe_urls.fitmencook import FitMenCookScraper
from recipe_urls.fitslowcookerqueen import FitSlowCookerQueenScraper
from recipe_urls.food import FoodScraper
from recipe_urls.food52 import Food52Scraper
from recipe_urls.foodandwine import FoodAndWineScraper
from recipe_urls.foodnetwork import FoodNetworkScraper
from recipe_urls.foodrepublic import FoodRepublicScraper
from recipe_urls.forksoverknives import ForksOverKnivesScraper
from recipe_urls.forktospoon import ForkToSpoonScraper
from recipe_urls.gimmesomeoven import GimmeSomeOvenScraper
from recipe_urls.gonnawantseconds import GonnaWantSecondsScraper
from recipe_urls.goodfooddiscoveries import GoodFoodDiscoveriesScraper
from recipe_urls.goodhousekeeping import GoodHousekeepingScraper
from recipe_urls.greatbritishchefs import GreatBritishChefsScraper
from recipe_urls.halfbakedharvest import HalfbakedHarvestScraper
from recipe_urls.hellofresh import HelloFreshScraper
from recipe_urls.ninjatestkitchen import NinjaTestKitchenScraper
from recipe_urls.nytimes import NyTimesScraper


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
    DomesticateMeScraper.host(): DomesticateMeScraper, 
    DownshiftologyScraper.host(): DownshiftologyScraper, 
    EatingBirdFoodScraper.host(): EatingBirdFoodScraper, 
    EatingWellScraper.host(): EatingWellScraper,
    EatLiveRunScraper.host(): EatLiveRunScraper,
    EatSmarterScraper.host(): EatSmarterScraper,
    EatWell101Scraper.host(): EatWell101Scraper,
    EatWhatTonightScraper.host(): EatWhatTonightScraper, 
    ElaVeganScraper.host(): ElaVeganScraper,
    EpicuriousScraper.host(): EpicuriousScraper,
    ErrensKitchenScraper.host(): ErrensKitchenScraper,
    EthanChlebowskiScraper.host(): EthanChlebowskiScraper, 
    FarmhouseOnBooneScraper.host(): FarmhouseOnBooneScraper,
    FifteenSpatulasScraper.host(): FifteenSpatulasScraper,
    FineDiningLoversScraper.host(): FineDiningLoversScraper,
    FitMenCookScraper.host(): FitMenCookScraper,
    FitSlowCookerQueenScraper.host(): FitSlowCookerQueenScraper, 
    FoodScraper.host(): FoodScraper, 
    Food52Scraper.host(): Food52Scraper, 
    FoodAndWineScraper.host(): FoodAndWineScraper,
    FoodNetworkScraper.host(): FoodNetworkScraper,
    FoodRepublicScraper.host(): FoodRepublicScraper,
    ForksOverKnivesScraper.host(): ForksOverKnivesScraper, 
    ForkToSpoonScraper.host(): ForkToSpoonScraper,
    GimmeSomeOvenScraper.host(): GimmeSomeOvenScraper, 
    GonnaWantSecondsScraper.host(): GonnaWantSecondsScraper, 
    GoodFoodDiscoveriesScraper.host(): GoodFoodDiscoveriesScraper,
    GoodHousekeepingScraper.host(): GoodHousekeepingScraper, 
    GreatBritishChefsScraper.host(): GreatBritishChefsScraper, 
    HalfbakedHarvestScraper.host(): HalfbakedHarvestScraper, 
    HelloFreshScraper.host(): HelloFreshScraper, 
    NinjaTestKitchenScraper.host(): NinjaTestKitchenScraper, 
    NyTimesScraper.host(): NyTimesScraper
}

def scrape_urls(base_url: str) -> Optional[AbstractScraper]:
    try:
        scraper_class = SCRAPERS.get(get_site_origin(base_url))
        if not scraper_class:
            raise ValueError(f"Unsupported website {base_url}")

        scraper_instance = scraper_class(base_url)
        return scraper_instance.scrape()

    # except httpx.HTTPError as e:
    #     if isinstance(e.cause, httpcore.ReadTimeout):
    #         raise TimeoutError("Request timed out.")
    #     elif e.status_code == 404:
    #         raise ValueError(f"URL not found {e.request.url}")
    #     else:
    #         raise httpx.HTTPError(f"HTTP error for {base_url}: {e}") from None

    except Exception as e:
        raise e from None
