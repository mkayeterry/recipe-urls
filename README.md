# recipe-urls (Under Development)

## Overview

`recipe-urls` is a Python package designed to gather recipe URLs from a given base URL.

## Installation

Note: This package is currently under development and not available for installation through pip.

<!-- https://```bash
pip install recipe-urls
``` -->

## Usage

```python
from recipe_urls import scrape_urls
```

## Example usage

```python
base_urls = ['https://bakingmischief.com', 'https://www.allrecipes.com']
compiled_recipe_links = []

for base_url in base_urls:
    try:
        scrape = scrape_urls(base_url)
        compiled_recipe_links.extend(scrape)
    except Exception as e:
        print(e)
```

## Supported Websites (So Far!)

- https://abuelascounter.com
- https:/www.acouplecooks.com
- https://addapinch.com
- https://www.afghankitchenrecipes.com
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
- https://ninjatestkitchen.eu
- https://cooking.nytimes.com


## License

This project is licensed under the MIT License - https://see the [LICENSE](LICENSE) file for details.