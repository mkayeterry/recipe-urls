# recipe-urls

## Overview

`recipe-urls` is a Python package designed to gather recipe URLs from a given base URL or from provided html content.

<br>

## Installation

```bash
pip install recipe-urls
```

## Usage

```python
from recipe_urls import scrape_urls, scrape_html
```

## Example usage

```python
base_urls = ['https://bakingmischief.com', 'https://www.allrecipes.com/recipes/80/main-dish/']
compiled_recipe_links = []

for base_url in base_urls:
    scraped_links = scrape_urls(base_url)
    compiled_recipe_links.extend(scraped_links)
```
```python
input_html = [baking_mischief_html, all_recipes_html]
compiled_recipe_links = []

for html_content in input_html:
    scraped_links = scrape_html(html) # optionally, scrape_html(html, base_url)
    compiled_recipe_links.extend(scraped_links)
```

## Supported Websites

- https://abuelascounter.com
- https://www.acouplecooks.com
- https://addapinch.com
- http://www.afghankitchenrecipes.com
- https://www.allrecipes.com
- https://www.ambitiouskitchen.com
- https://www.archanaskitchen.com
- https://www.averiecooks.com
- https://bakingmischief.com
- https://www.baking-sense.com
- https://barefootcontessa.com
- https://www.bbc.co.uk
- https://www.bettycrocker.com
- https://www.bigoven.com
- https://bluejeanchef.com
- https://www.bonappetit.com
- https://www.bongeats.com
- https://www.bowlofdelicious.com
- https://www.budgetbytes.com
- https://carlsbadcravings.com
- https://www.castironketo.net
- https://www.cdkitchen.com
- https://chefsavvy.com
- https://www.closetcooking.com
- https://cookieandkate.com
- https://copykat.com 
- https://www.countryliving.com
- https://creativecanning.com
- https://www.davidlebovitz.com
- https://www.delish.com
- https://domesticate-me.com
- https://downshiftology.com
- https://www.eatingbirdfood.com
- https://www.eatingwell.com
- https://www.eatliverun.com
- https://eatsmarter.com
- https://www.eatwell101.com
- https://eatwhattonight.com
- https://elavegan.com
- https://www.ethanchlebowski.com
- https://www.errenskitchen.com
- https://www.epicurious.com
- https://www.farmhouseonboone.com
- https://www.fifteenspatulas.com
- https://www.finedininglovers.com
- https://fitmencook.com
- https://fitslowcookerqueen.com
- https://www.food.com
- https://food52.com
- https://www.foodandwine.com
- https://www.foodnetwork.com
- https://www.foodrepublic.com
- https://www.forksoverknives.com
- https://forktospoon.com
- https://www.gimmesomeoven.com
- https://www.gonnawantseconds.com
- https://goodfooddiscoveries.com
- https://www.goodhousekeeping.com
- https://www.greatbritishchefs.com
- https://www.halfbakedharvest.com
- https://handletheheat.com
- https://headbangerskitchen.com
- https://heatherchristo.com
- https://www.hellofresh.com
- https://www.hersheyland.com
- https://hostthetoast.com
- https://im-worthy.com
- https://www.indianhealthyrecipes.com
- https://insanelygoodrecipes.com
- https://inspiralized.com
- https://izzycooking.com
- https://www.jamieoliver.com
- https://jimcooksfoodgood.com
- https://joyfoodsunshine.com
- https://www.justataste.com
- https://justbento.com
- https://www.justonecookbook.com
- https://www.kingarthurbaking.com
- https://leanandgreenrecipes.net
- https://lifestyleofafoodie.com
- https://littlespicejar.com
- https://livelytable.com
- https://lovingitvegan.com
- https://ninjatestkitchen.eu
- https://cooking.nytimes.com
- https://ohsheglows.com
- https://www.onceuponachef.com
- https://www.paleorunningmomma.com
- https://www.persnicketyplates.com
- https://www.pickuplimes.com
- https://www.platingpixels.com
- https://rachlmansfield.com
- https://rainbowplantlife.com
- https://reciperunner.com
- https://sallysbakingaddiction.com
- https://simple-veganista.com
- https://www.simplywhisked.com
- https://www.tasteofhome.com
- https://tasty.co
- https://www.wellplated.com
- https://whole30.com


## Acknowledgments 
This package was inspired by (and meant to be used in conjunction with) [recipe-scrapers](https://github.com/hhursev/recipe-scrapers) by [hhursev](https://github.com/hhursev). Thanks for making the intersection of programming and recipes more doable!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.