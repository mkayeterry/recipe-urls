import csv
import os
import pytest
from bs4 import BeautifulSoup
from importlib import import_module

CONFIG = {"scraper_dir": "recipe_urls", "test_dir": "tests/test_data"}


def get_scraper_modules():
    modules = []
    for module_file in os.listdir(CONFIG["scraper_dir"]):
        if module_file.endswith(".py") and not module_file.startswith("_"):
            module_name = module_file[:-3]
            modules.append(
                (module_name, import_module(f'{CONFIG["scraper_dir"]}.{module_name}'))
            )
    return modules


def get_test_files():
    for dirpath, dirnames, filenames in os.walk(CONFIG["test_dir"]):
        html_file = next((f for f in filenames if f.endswith(".testhtml")), None)
        exp_output_file = next(
            (f for f in filenames if f.endswith("_exp_output.csv")), None
        )
        if html_file and exp_output_file:
            yield (
                os.path.join(dirpath, html_file),
                os.path.join(dirpath, exp_output_file),
            )


def load_base_url(dirpath):
    base_url_file = next(
        (f for f in os.listdir(dirpath) if f.endswith("_base_url.csv")), None
    )
    if base_url_file:
        with open(os.path.join(dirpath, base_url_file), newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                return row[0]


def find_class(module, base_name):
    target_name = base_name.lower() + "scraper"
    for name in dir(module):
        if name.lower() == target_name:
            return getattr(module, name)
    raise AttributeError(
        f"Module '{module.__name__}' does not have a class matching '{base_name}Scraper'"
    )


@pytest.mark.parametrize(
    "scraper_module, html_file, exp_output_file",
    [
        (module, html, exp_output)
        for module in get_scraper_modules()
        for html, exp_output in get_test_files()
        if module[0] == os.path.basename(html)[:-9]
    ],
)
def test_scraper(mocker, scraper_module, html_file, exp_output_file):
    module_name, module = scraper_module
    scraper_class = find_class(module, module_name)

    # Determine the base URL from the associated CSV file
    base_url = load_base_url(os.path.dirname(html_file))

    # Read the HTML content from the file
    with open(html_file, "r") as file:
        html_content = file.read()

    # Instantiate the scraper using the HTML content and the loaded base URL
    scraper = scraper_class(base_url=base_url, html=html_content)

    # Perform the scraping
    scraped_links = scraper.scrape()

    # Load expected results
    expected_links = []
    with open(exp_output_file, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            expected_links.extend(row)

    # Assert that the scraped links match the expected links
    assert set(scraped_links) == set(
        expected_links
    ), f"The scraped links do not match the expected links for {module_name}."
