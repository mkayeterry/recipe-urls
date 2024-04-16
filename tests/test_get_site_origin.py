import pytest

from recipe_urls import _utils


def test_get_site_origin_random():
    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("")


def test_get_site_origin_example():
    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("https://example.com")


def test_get_site_origin_none():
    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin(None)


def test_get_site_origin_numbers():
    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin(123)


def test_get_site_origin_invalid():
    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("invalid_url")


def test_get_site_origin_list():
    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin(["https://example.com"])


def test_get_site_origin_dict():
    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin({"url": "https://example.com"})


def test_get_site_origin_abuelascounter():
    assert _utils.get_site_origin("https://abuelascounter.com") == 'abuelascounter.com'
    assert _utils.get_site_origin("abuelascounter.com") == 'abuelascounter.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.abuelascounter.com")


def test_get_site_origin_acouplecooks():
    assert _utils.get_site_origin("https://www.acouplecooks.com") == 'www.acouplecooks.com'
    assert _utils.get_site_origin("www.acouplecooks.com") == 'www.acouplecooks.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("acouplecooks.com")


def test_get_site_origin_addapinch():
    assert _utils.get_site_origin("https://addapinch.com") == 'addapinch.com'
    assert _utils.get_site_origin("addapinch.com") == 'addapinch.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.addapinch.com")


def test_get_site_origin_afghankitchenrecipes():
    assert _utils.get_site_origin("https://www.afghankitchenrecipes.com") == 'www.afghankitchenrecipes.com'
    assert _utils.get_site_origin("www.afghankitchenrecipes.com") == 'www.afghankitchenrecipes.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("afghankitchenrecipes.com")


def test_get_site_origin_allrecipes():
    assert _utils.get_site_origin("https://www.allrecipes.com") == 'www.allrecipes.com'
    assert _utils.get_site_origin("www.allrecipes.com") == 'www.allrecipes.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("allrecipes.com")


def test_get_site_origin_ambitiouskitchen():
    assert _utils.get_site_origin("https://www.ambitiouskitchen.com") == 'www.ambitiouskitchen.com'
    assert _utils.get_site_origin("www.ambitiouskitchen.com") == 'www.ambitiouskitchen.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("ambitiouskitchen.com")


def test_get_site_origin_archanaskitchen():
    assert _utils.get_site_origin("https://www.archanaskitchen.com") == 'www.archanaskitchen.com'
    assert _utils.get_site_origin("www.archanaskitchen.com") == 'www.archanaskitchen.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("archanaskitchen.com")


def test_get_site_origin_averiecooks():
    assert _utils.get_site_origin("https://www.averiecooks.com") == 'www.averiecooks.com'
    assert _utils.get_site_origin("www.averiecooks.com") == 'www.averiecooks.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("averiecooks.com")


def test_get_site_origin_bakingmischief():
    assert _utils.get_site_origin("https://bakingmischief.com") == 'bakingmischief.com'
    assert _utils.get_site_origin("bakingmischief.com") == 'bakingmischief.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.bakingmischief.com")


def test_get_site_origin_bakingsense():
    assert _utils.get_site_origin("https://www.baking-sense.com") == 'www.baking-sense.com'
    assert _utils.get_site_origin("www.baking-sense.com") == 'www.baking-sense.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("baking-sense.com")


def test_get_site_origin_barefootcontessa():
    assert _utils.get_site_origin("https://barefootcontessa.com") == 'barefootcontessa.com'
    assert _utils.get_site_origin("barefootcontessa.com") == 'barefootcontessa.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.barefootcontessa.com")


def test_get_site_origin_bbc():
    assert _utils.get_site_origin("https://www.bbc.co.uk") == 'www.bbc.co.uk'
    assert _utils.get_site_origin("www.bbc.co.uk") == 'www.bbc.co.uk'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("bbc.co.uk")


def test_get_site_origin_bettycrocker():
    assert _utils.get_site_origin("https://www.bettycrocker.com") == 'www.bettycrocker.com'
    assert _utils.get_site_origin("www.bettycrocker.com") == 'www.bettycrocker.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("bettycrocker.com")


def test_get_site_origin_bigoven():
    assert _utils.get_site_origin("https://www.bigoven.com") == 'www.bigoven.com'
    assert _utils.get_site_origin("www.bigoven.com") == 'www.bigoven.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("bigoven.com")


def test_get_site_origin_bluejeanchef():
    assert _utils.get_site_origin("https://bluejeanchef.com") == 'bluejeanchef.com'
    assert _utils.get_site_origin("bluejeanchef.com") == 'bluejeanchef.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.bluejeanchef.com")


def test_get_site_origin_bonappetit():
    assert _utils.get_site_origin("https://www.bonappetit.com") == 'www.bonappetit.com'
    assert _utils.get_site_origin("www.bonappetit.com") == 'www.bonappetit.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("bonappetit.com")


def test_get_site_origin_bongeats():
    assert _utils.get_site_origin("https://www.bongeats.com") == 'www.bongeats.com'
    assert _utils.get_site_origin("www.bongeats.com") == 'www.bongeats.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("bongeats.com")


def test_get_site_origin_bowlofdelicious():
    assert _utils.get_site_origin("https://www.bowlofdelicious.com") == 'www.bowlofdelicious.com'
    assert _utils.get_site_origin("www.bowlofdelicious.com") == 'www.bowlofdelicious.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("bowlofdelicious.com")


def test_get_site_origin_budgetbytes():
    assert _utils.get_site_origin("https://www.budgetbytes.com") == 'www.budgetbytes.com'
    assert _utils.get_site_origin("www.budgetbytes.com") == 'www.budgetbytes.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("budgetbytes.com")


def test_get_site_origin_carlsbadcravings():
    assert _utils.get_site_origin("https://carlsbadcravings.com") == 'carlsbadcravings.com'
    assert _utils.get_site_origin("carlsbadcravings.com") == 'carlsbadcravings.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.carlsbadcravings.com")


def test_get_site_origin_castironketo():
    assert _utils.get_site_origin("https://www.castironketo.net") == 'www.castironketo.net'
    assert _utils.get_site_origin("www.castironketo.net") == 'www.castironketo.net'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("castironketo.net")


def test_get_site_origin_cdkitchen():
    assert _utils.get_site_origin("https://www.cdkitchen.com") == 'www.cdkitchen.com'
    assert _utils.get_site_origin("www.cdkitchen.com") == 'www.cdkitchen.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("cdkitchen.com")


def test_get_site_origin_chefsavvy():
    assert _utils.get_site_origin("https://chefsavvy.com") == 'chefsavvy.com'
    assert _utils.get_site_origin("chefsavvy.com") == 'chefsavvy.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.chefsavvy.com")


def test_get_site_origin_closetcooking():
    assert _utils.get_site_origin("https://www.closetcooking.com") == 'www.closetcooking.com'
    assert _utils.get_site_origin("www.closetcooking.com") == 'www.closetcooking.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("closetcooking.com")


def test_get_site_origin_cookieandkate():
    assert _utils.get_site_origin("https://cookieandkate.com") == 'cookieandkate.com'
    assert _utils.get_site_origin("cookieandkate.com") == 'cookieandkate.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.cookieandkate.com")


def test_get_site_origin_copykat():
    assert _utils.get_site_origin("https://copykat.com") == 'copykat.com'
    assert _utils.get_site_origin("copykat.com") == 'copykat.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.copykat.com")


def test_get_site_origin_countryliving():
    assert _utils.get_site_origin("https://www.countryliving.com") == 'www.countryliving.com'
    assert _utils.get_site_origin("www.countryliving.com") == 'www.countryliving.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("countryliving.com")


def test_get_site_origin_creativecanning():
    assert _utils.get_site_origin("https://creativecanning.com") == 'creativecanning.com'
    assert _utils.get_site_origin("creativecanning.com") == 'creativecanning.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.creativecanning.com")


def test_get_site_origin_davidlebovitz():
    assert _utils.get_site_origin("https://www.davidlebovitz.com") == 'www.davidlebovitz.com'
    assert _utils.get_site_origin("www.davidlebovitz.com") == 'www.davidlebovitz.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("davidlebovitz.com")


def test_get_site_origin_delish():
    assert _utils.get_site_origin("https://www.delish.com") == 'www.delish.com'
    assert _utils.get_site_origin("www.delish.com") == 'www.delish.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("delish.com")


def test_get_site_origin_domesticate_me():
    assert _utils.get_site_origin("https://domesticate-me.com") == 'domesticate-me.com'
    assert _utils.get_site_origin("domesticate-me.com") == 'domesticate-me.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.domesticate-me.com")


def test_get_site_origin_downshiftology():
    assert _utils.get_site_origin("https://downshiftology.com") == 'downshiftology.com'
    assert _utils.get_site_origin("downshiftology.com") == 'downshiftology.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.downshiftology.com")


def test_get_site_origin_eatingbirdfood():
    assert _utils.get_site_origin("https://www.eatingbirdfood.com") == 'www.eatingbirdfood.com'
    assert _utils.get_site_origin("www.eatingbirdfood.com") == 'www.eatingbirdfood.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("eatingbirdfood.com")


def test_get_site_origin_eatingwell():
    assert _utils.get_site_origin("https://www.eatingwell.com") == 'www.eatingwell.com'
    assert _utils.get_site_origin("www.eatingwell.com") == 'www.eatingwell.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("eatingwell.com")


def test_get_site_origin_eatliverun():
    assert _utils.get_site_origin("https://www.eatliverun.com") == 'www.eatliverun.com'
    assert _utils.get_site_origin("www.eatliverun.com") == 'www.eatliverun.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("eatliverun.com")


def test_get_site_origin_eatsmarter():
    assert _utils.get_site_origin("https://eatsmarter.com") == 'eatsmarter.com'
    assert _utils.get_site_origin("eatsmarter.com") == 'eatsmarter.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.eatsmarter.com")


def test_get_site_origin_eatwell101():
    assert _utils.get_site_origin("https://www.eatwell101.com") == 'www.eatwell101.com'
    assert _utils.get_site_origin("www.eatwell101.com") == 'www.eatwell101.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("eatwell101.com")


def test_get_site_origin_eatwhattonight():
    assert _utils.get_site_origin("https://eatwhattonight.com") == 'eatwhattonight.com'
    assert _utils.get_site_origin("eatwhattonight.com") == 'eatwhattonight.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.eatwhattonight.com")


def test_get_site_origin_elavegan():
    assert _utils.get_site_origin("https://elavegan.com") == 'elavegan.com'
    assert _utils.get_site_origin("elavegan.com") == 'elavegan.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.elavegan.com")


def test_get_site_origin_ethanchlebowski():
    assert _utils.get_site_origin("https://www.ethanchlebowski.com") == 'www.ethanchlebowski.com'
    assert _utils.get_site_origin("www.ethanchlebowski.com") == 'www.ethanchlebowski.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("ethanchlebowski.com")


def test_get_site_origin_errenskitchen():
    assert _utils.get_site_origin("https://www.errenskitchen.com") == 'www.errenskitchen.com'
    assert _utils.get_site_origin("www.errenskitchen.com") == 'www.errenskitchen.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("errenskitchen.com")


def test_get_site_origin_epicurious():
    assert _utils.get_site_origin("https://www.epicurious.com") == 'www.epicurious.com'
    assert _utils.get_site_origin("www.epicurious.com") == 'www.epicurious.com'
    
    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("epicurious.com")


def test_get_site_origin_farmhouseonboone():
    assert _utils.get_site_origin("https://www.farmhouseonboone.com") == 'www.farmhouseonboone.com'
    assert _utils.get_site_origin("www.farmhouseonboone.com") == 'www.farmhouseonboone.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("farmhouseonboone.com")


def test_get_site_origin_fifteenspatulas():
    assert _utils.get_site_origin("https://www.fifteenspatulas.com") == 'www.fifteenspatulas.com'
    assert _utils.get_site_origin("www.fifteenspatulas.com") == 'www.fifteenspatulas.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("fifteenspatulas.com")


def test_get_site_origin_finedininglovers():
    assert _utils.get_site_origin("https://www.finedininglovers.com") == 'www.finedininglovers.com'
    assert _utils.get_site_origin("www.finedininglovers.com") == 'www.finedininglovers.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("finedininglovers.com")


def test_get_site_origin_fitmencook():
    assert _utils.get_site_origin("https://fitmencook.com") == 'fitmencook.com'
    assert _utils.get_site_origin("fitmencook.com") == 'fitmencook.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.fitmencook.com")


def test_get_site_origin_fitslowcookerqueen():
    assert _utils.get_site_origin("https://fitslowcookerqueen.com") == 'fitslowcookerqueen.com'
    assert _utils.get_site_origin("fitslowcookerqueen.com") == 'fitslowcookerqueen.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.fitslowcookerqueen.com")


def test_get_site_origin_fooddotcom():
    assert _utils.get_site_origin("https://www.food.com") == 'www.food.com'
    assert _utils.get_site_origin("www.food.com") == 'www.food.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("food.com")


def test_get_site_origin_food52():
    assert _utils.get_site_origin("https://food52.com") == 'food52.com'
    assert _utils.get_site_origin("food52.com") == 'food52.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.food52.com")


def test_get_site_origin_foodandwine():
    assert _utils.get_site_origin("https://www.foodandwine.com") == 'www.foodandwine.com'
    assert _utils.get_site_origin("www.foodandwine.com") == 'www.foodandwine.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("foodandwine.com")


def test_get_site_origin_foodnetwork():
    assert _utils.get_site_origin("https://www.foodnetwork.com") == 'www.foodnetwork.com'
    assert _utils.get_site_origin("www.foodnetwork.com") == 'www.foodnetwork.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("foodnetwork.com")


def test_get_site_origin_foodrepublic():
    assert _utils.get_site_origin("https://www.foodrepublic.com") == 'www.foodrepublic.com'
    assert _utils.get_site_origin("www.foodrepublic.com") == 'www.foodrepublic.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("foodrepublic.com")


def test_get_site_origin_forksoverknives():
    assert _utils.get_site_origin("https://www.forksoverknives.com") == 'www.forksoverknives.com'
    assert _utils.get_site_origin("www.forksoverknives.com") == 'www.forksoverknives.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("forksoverknives.com")


def test_get_site_origin_forktospoon():
    assert _utils.get_site_origin("https://forktospoon.com") == 'forktospoon.com'
    assert _utils.get_site_origin("forktospoon.com") == 'forktospoon.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.forktospoon.com")


def test_get_site_origin_gimmesomeoven():
    assert _utils.get_site_origin("https://www.gimmesomeoven.com") == 'www.gimmesomeoven.com'
    assert _utils.get_site_origin("www.gimmesomeoven.com") == 'www.gimmesomeoven.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("gimmesomeoven.com")


def test_get_site_origin_gonnawantseconds():
    assert _utils.get_site_origin("https://www.gonnawantseconds.com") == 'www.gonnawantseconds.com'
    assert _utils.get_site_origin("www.gonnawantseconds.com") == 'www.gonnawantseconds.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("gonnawantseconds.com")


def test_get_site_origin_goodfooddiscoveries():
    assert _utils.get_site_origin("https://goodfooddiscoveries.com") == 'goodfooddiscoveries.com'
    assert _utils.get_site_origin("goodfooddiscoveries.com") == 'goodfooddiscoveries.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.goodfooddiscoveries.com")


def test_get_site_origin_goodhousekeeping():
    assert _utils.get_site_origin("https://www.goodhousekeeping.com") == 'www.goodhousekeeping.com'
    assert _utils.get_site_origin("www.goodhousekeeping.com") == 'www.goodhousekeeping.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("goodhousekeeping.com")


def test_get_site_origin_greatbritishchefs():
    assert _utils.get_site_origin("https://www.greatbritishchefs.com") == 'www.greatbritishchefs.com'
    assert _utils.get_site_origin("www.greatbritishchefs.com") == 'www.greatbritishchefs.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("greatbritishchefs.com")


def test_get_site_origin_halfbakedharvest():
    assert _utils.get_site_origin("https://www.halfbakedharvest.com") == 'www.halfbakedharvest.com'
    assert _utils.get_site_origin("www.halfbakedharvest.com") == 'www.halfbakedharvest.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("halfbakedharvest.com")


def test_get_site_origin_handletheheat():
    assert _utils.get_site_origin("https://handletheheat.com") == 'handletheheat.com'
    assert _utils.get_site_origin("handletheheat.com") == 'handletheheat.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.handletheheat.com")


def test_get_site_origin_headbangerskitchen():
    assert _utils.get_site_origin("https://headbangerskitchen.com") == 'headbangerskitchen.com'
    assert _utils.get_site_origin("headbangerskitchen.com") == 'headbangerskitchen.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.headbangerskitchen.com")


def test_get_site_origin_heatherchristo():
    assert _utils.get_site_origin("https://heatherchristo.com") == 'heatherchristo.com'
    assert _utils.get_site_origin("heatherchristo.com") == 'heatherchristo.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.heatherchristo.com")


def test_get_site_origin_hellofresh():
    assert _utils.get_site_origin("https://www.hellofresh.com") == 'www.hellofresh.com'
    assert _utils.get_site_origin("www.hellofresh.com") == 'www.hellofresh.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("hellofresh.com")


def test_get_site_origin_hersheyland():
    assert _utils.get_site_origin("https://www.hersheyland.com") == 'www.hersheyland.com'
    assert _utils.get_site_origin("www.hersheyland.com") == 'www.hersheyland.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("hersheyland.com")


def test_get_site_origin_hostthetoast():
    assert _utils.get_site_origin("https://hostthetoast.com") == 'hostthetoast.com'
    assert _utils.get_site_origin("hostthetoast.com") == 'hostthetoast.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.hostthetoast.com")


def test_get_site_origin_imworthy():
    assert _utils.get_site_origin("https://im-worthy.com") == 'im-worthy.com'
    assert _utils.get_site_origin("im-worthy.com") == 'im-worthy.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.im-worthy.com")


def test_get_site_origin_indianhealthyrecipes():
    assert _utils.get_site_origin("https://www.indianhealthyrecipes.com") == 'www.indianhealthyrecipes.com'
    assert _utils.get_site_origin("www.indianhealthyrecipes.com") == 'www.indianhealthyrecipes.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("indianhealthyrecipes.com")


def test_get_site_origin_insanelygoodrecipes():
    assert _utils.get_site_origin("https://insanelygoodrecipes.com") == 'insanelygoodrecipes.com'
    assert _utils.get_site_origin("insanelygoodrecipes.com") == 'insanelygoodrecipes.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.insanelygoodrecipes.com")


def test_get_site_origin_inspiralized():
    assert _utils.get_site_origin("https://inspiralized.com") == 'inspiralized.com'
    assert _utils.get_site_origin("inspiralized.com") == 'inspiralized.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.inspiralized.com")


def test_get_site_origin_izzycooking():
    assert _utils.get_site_origin("https://izzycooking.com") == 'izzycooking.com'
    assert _utils.get_site_origin("izzycooking.com") == 'izzycooking.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.izzycooking.com")


def test_get_site_origin_jamieoliver():
    assert _utils.get_site_origin("https://www.jamieoliver.com") == 'www.jamieoliver.com'
    assert _utils.get_site_origin("www.jamieoliver.com") == 'www.jamieoliver.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("jamieoliver.com")


def test_get_site_origin_jimcooksfoodgood():
    assert _utils.get_site_origin("https://jimcooksfoodgood.com") == 'jimcooksfoodgood.com'
    assert _utils.get_site_origin("jimcooksfoodgood.com") == 'jimcooksfoodgood.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.jimcooksfoodgood.com")


def test_get_site_origin_joyfoodsunshine():
    assert _utils.get_site_origin("https://joyfoodsunshine.com") == 'joyfoodsunshine.com'
    assert _utils.get_site_origin("joyfoodsunshine.com") == 'joyfoodsunshine.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.joyfoodsunshine.com")


def test_get_site_origin_justataste():
    assert _utils.get_site_origin("https://www.justataste.com") == 'www.justataste.com'
    assert _utils.get_site_origin("www.justataste.com") == 'www.justataste.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("justataste.com")


def test_get_site_origin_justbento():
    assert _utils.get_site_origin("https://justbento.com") == 'justbento.com'
    assert _utils.get_site_origin("justbento.com") == 'justbento.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.justbento.com")


def test_get_site_origin_justonecookbook():
    assert _utils.get_site_origin("https://www.justonecookbook.com") == 'www.justonecookbook.com'
    assert _utils.get_site_origin("www.justonecookbook.com") == 'www.justonecookbook.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("justonecookbook.com")


def test_get_site_origin_kingarthurbaking():
    assert _utils.get_site_origin("https://www.kingarthurbaking.com") == 'www.kingarthurbaking.com'
    assert _utils.get_site_origin("www.kingarthurbaking.com") == 'www.kingarthurbaking.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("kingarthurbaking.com")


def test_get_site_origin_leanandgreenrecipes():
    assert _utils.get_site_origin("https://leanandgreenrecipes.net") == 'leanandgreenrecipes.net'
    assert _utils.get_site_origin("leanandgreenrecipes.net") == 'leanandgreenrecipes.net'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.leanandgreenrecipes.net")


def test_get_site_origin_lifestyleofafoodie():
    assert _utils.get_site_origin("https://lifestyleofafoodie.com") == 'lifestyleofafoodie.com'
    assert _utils.get_site_origin("lifestyleofafoodie.com") == 'lifestyleofafoodie.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.lifestyleofafoodie.com")


def test_get_site_origin_littlespicejar():
    assert _utils.get_site_origin("https://littlespicejar.com") == 'littlespicejar.com'
    assert _utils.get_site_origin("littlespicejar.com") == 'littlespicejar.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.littlespicejar.com")


def test_get_site_origin_livelytable():
    assert _utils.get_site_origin("https://livelytable.com") == 'livelytable.com'
    assert _utils.get_site_origin("livelytable.com") == 'livelytable.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.livelytable.com")


def test_get_site_origin_lovingitvegan():
    assert _utils.get_site_origin("https://lovingitvegan.com") == 'lovingitvegan.com'
    assert _utils.get_site_origin("lovingitvegan.com") == 'lovingitvegan.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.lovingitvegan.com")


def test_get_site_origin_ninjatestkitchen():
    assert _utils.get_site_origin("https://ninjatestkitchen.eu") == 'ninjatestkitchen.eu'
    assert _utils.get_site_origin("ninjatestkitchen.eu") == 'ninjatestkitchen.eu'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.ninjatestkitchen.eu")


def test_get_site_origin_nytimescooking():
    assert _utils.get_site_origin("https://cooking.nytimes.com") == 'cooking.nytimes.com'
    assert _utils.get_site_origin("cooking.nytimes.com") == 'cooking.nytimes.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.nytimes.com")


def test_get_site_origin_ohsheglows():
    assert _utils.get_site_origin("https://ohsheglows.com") == 'ohsheglows.com'
    assert _utils.get_site_origin("ohsheglows.com") == 'ohsheglows.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.ohsheglows.com")


def test_get_site_origin_onceuponachef():
    assert _utils.get_site_origin("https://www.onceuponachef.com") == 'www.onceuponachef.com'
    assert _utils.get_site_origin("www.onceuponachef.com") == 'www.onceuponachef.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("onceuponachef.com")


def test_get_site_origin_paleorunningmomma():
    assert _utils.get_site_origin("https://www.paleorunningmomma.com") == 'www.paleorunningmomma.com'
    assert _utils.get_site_origin("www.paleorunningmomma.com") == 'www.paleorunningmomma.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("paleorunningmomma.com")


def test_get_site_origin_persnicketyplates():
    assert _utils.get_site_origin("https://www.persnicketyplates.com") == 'www.persnicketyplates.com'
    assert _utils.get_site_origin("www.persnicketyplates.com") == 'www.persnicketyplates.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("persnicketyplates.com")


def test_get_site_origin_pickuplimes():
    assert _utils.get_site_origin("https://www.pickuplimes.com") == 'www.pickuplimes.com'
    assert _utils.get_site_origin("www.pickuplimes.com") == 'www.pickuplimes.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("pickuplimes.com")


def test_get_site_origin_platingpixels():
    assert _utils.get_site_origin("https://www.platingpixels.com") == 'www.platingpixels.com'
    assert _utils.get_site_origin("www.platingpixels.com") == 'www.platingpixels.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("platingpixels.com")


def test_get_site_origin_rachlmansfield():
    assert _utils.get_site_origin("https://rachlmansfield.com") == 'rachlmansfield.com'
    assert _utils.get_site_origin("rachlmansfield.com") == 'rachlmansfield.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.rachlmansfield.com")


def test_get_site_origin_rainbowplantlife():
    assert _utils.get_site_origin("https://rainbowplantlife.com") == 'rainbowplantlife.com'
    assert _utils.get_site_origin("rainbowplantlife.com") == 'rainbowplantlife.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.rainbowplantlife.com")


def test_get_site_origin_reciperunner():
    assert _utils.get_site_origin("https://reciperunner.com") == 'reciperunner.com'
    assert _utils.get_site_origin("reciperunner.com") == 'reciperunner.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.reciperunner.com")


def test_get_site_origin_sallysbakingaddiction():
    assert _utils.get_site_origin("https://sallysbakingaddiction.com") == 'sallysbakingaddiction.com'
    assert _utils.get_site_origin("sallysbakingaddiction.com") == 'sallysbakingaddiction.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.sallysbakingaddiction.com")


def test_get_site_origin_simpleveganista():
    assert _utils.get_site_origin("https://simple-veganista.com") == 'simple-veganista.com'
    assert _utils.get_site_origin("simple-veganista.com") == 'simple-veganista.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.simple-veganista.com")


def test_get_site_origin_simplywhisked():
    assert _utils.get_site_origin("https://www.simplywhisked.com") == 'www.simplywhisked.com'
    assert _utils.get_site_origin("www.simplywhisked.com") == 'www.simplywhisked.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("simplywhisked.com")


def test_get_site_origin_tasteofhome():
    assert _utils.get_site_origin("https://www.tasteofhome.com") == 'www.tasteofhome.com'
    assert _utils.get_site_origin("www.tasteofhome.com") == 'www.tasteofhome.com'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("tasteofhome.com")


def test_get_site_origin_tasty():
    assert _utils.get_site_origin("https://tasty.co") == 'tasty.co'
    assert _utils.get_site_origin("tasty.co") == 'tasty.co'

    with pytest.raises(ValueError, match=r"not supported"):
        _utils.get_site_origin("www.tasty.co")
