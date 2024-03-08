# recipe-urls (Under Development)

## Overview

`recipe-urls` is a Python package designed to gather recipe URLs from a given base URL.

## Installation

Note: This package is currently under development and not available for installation through pip.

<!-- ```bash
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

- abuelascounter.com
- www.acouplecooks.com
- addapinch.com
- www.afghankitchenrecipes.com
- www.allrecipes.com
- www.ambitiouskitchen.com
- www.archanaskitchen.com
- www.averiecooks.com
- bakingmischief.com
- www.baking-sense.com
- barefootcontessa.com
- www.bbc.co.uk
- www.bettycrocker.com
- www.bigoven.com
- bluejeanchef.com
- www.bonappetit.com
- www.bongeats.com
- www.bowlofdelicious.com
- www.budgetbytes.com
- carlsbadcravings.com
- www.castironketo.net
- www.cdkitchen.com
- chefsavvy.com
- www.closetcooking.com
- cookieandkate.com
- copykat.com 
- www.countryliving.com
- creativecanning.com
- www.davidlebovitz.com
- www.delish.com
- domesticate-me.com
- downshiftology.com
- www.eatingbirdfood.com
- www.eatingwell.com
- www.eatliverun.com
- eatsmarter.com
- www.eatwell101.com
- eatwhattonight.com
- elavegan.com
- www.ethanchlebowski.com
- www.errenskitchen.com
- www.epicurious.com
- www.farmhouseonboone.com
- www.fifteenspatulas.com
- www.finedininglovers.com
- fitmencook.com
- fitslowcookerqueen.com
- www.food.com
- food52.com
- www.foodandwine.com
- www.foodnetwork.com
- www.foodrepublic.com
- www.forksoverknives.com
- forktospoon.com
- www.gimmesomeoven.com
- goodfooddiscoveries.com
- www.hellofresh.com
- ninjatestkitchen.eu
- cooking.nytimes.com


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.