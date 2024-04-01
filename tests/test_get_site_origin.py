import pytest

from recipe_urls import _utils


def test_get_site_origins_valid_allrecipes_url():

    assert _utils.get_site_origin("https://www.allrecipes.com") == 'www.allrecipes.com'

def test_get_site_origins_valid_fooddotcom_url():

    assert _utils.get_site_origin("https://www.food.com") == 'www.food.com'



