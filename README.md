# recipe-urls (Under Development)

## Overview

`recipe-urls` is a Python package designed to gather base URLs from recipe websites.

## Installation

**Note: This package is currently under development and not available for installation through pip.**

<!-- ```bash
pip install recipe-urls
``` -->

## Usage

```python
from recipe_urls import main
```

## Example usage
url = "https://www.allrecipes.com/recipe/12345/delicious-recipe/"
recipe_data = main.scrape_recipe(url)
print(recipe_data)

## Supported Websites (So Far!)

- [Afghan Kitchen Recipes](http://www.afghankitchenrecipes.com)
- [AllRecipes](https://www.allrecipes.com)
- [Averie Cooks](https://www.averiecooks.com)
- [Baking Sense](https://www.baking-sense.com)
- [Bong Eats](https://www.bongeats.com)
- [Food52](https://food52.com)
- [Food.com](https://www.food.com)
- [HelloFresh](https://www.hellofresh.com)
- [NYT Cooking](https://cooking.nytimes.com/)

## Acknowledgements

This package is intended to be used in conjunction with the [recipe-scrapers](https://github.com/hhursev/recipe-scrapers) package by hhursev. The inspiration for this project comes from the need to gather base URLs for recipe websites before utilizing recipe-scrapers for detailed recipe extraction.

## License

This project is licensed under the MIT License - see the LICENSE file for details.