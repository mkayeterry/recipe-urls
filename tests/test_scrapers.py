import pytest
import csv
import os
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
        csv_file = next((f for f in filenames if f.endswith(".csv")), None)
        if html_file and csv_file:
            yield (os.path.join(dirpath, html_file), os.path.join(dirpath, csv_file))


def load_html(file_path):
    try:
        with open(file_path, "r") as file:
            return BeautifulSoup(file.read(), "html.parser")
    except Exception as e:
        print(f"Error loading HTML file {file_path}: {e}")
        raise


def format_class_name(module_name):
    parts = module_name.split("_")
    class_name = "".join(part.capitalize() for part in parts) + "Scraper"
    return class_name


def find_class(module, base_name):
    target_name = base_name.lower() + "scraper"
    for name in dir(module):
        if name.lower() == target_name:
            return getattr(module, name)
    raise AttributeError(
        f"Module '{module.__name__}' does not have a class matching '{base_name}Scraper'"
    )


def strip_domain_from_urls(urls):
    stripped_urls = []
    for url in urls:
        path_parts = url.split("://")[-1].split("/")[1:]
        path = "/" + "/".join(path_parts)
        stripped_urls.append(path)
    return stripped_urls


@pytest.mark.parametrize(
    "scraper_module, html_file, csv_file",
    [
        (module, html, csv)
        for module in get_scraper_modules()
        for html, csv in get_test_files()
        if module[0] in os.path.basename(html)
    ],
)
def test_scraper(mocker, scraper_module, html_file, csv_file):
    module_name, module = scraper_module
    scraper_class = find_class(module, module_name)

    # Read the HTML content from the file
    with open(html_file, "r") as file:
        html_content = file.read()

    # Instantiate the scraper using the HTML content
    scraper = scraper_class(html=html_content)

    # Manually set the soup if not already set in the constructor
    if not hasattr(scraper, "soup"):
        scraper.soup = BeautifulSoup(html_content, "html.parser")

    # Perform the scraping
    scraped_links = scraper.scrape()

    # Strip the domain from scraped links dynamically
    scraped_links = strip_domain_from_urls(scraped_links)

    # Load expected results
    expected_links = []
    with open(csv_file, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            expected_links.extend(row)

    # Assert that the scraped links match the expected links
    assert sorted(scraped_links) == sorted(
        expected_links
    ), f"The scraped links do not match the expected links for {module_name}."
