import pytest
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from recipe_urls._utils import concat_host



@pytest.fixture
def sample_soup():
    # Sample HTML content for testing extract_base_domain function
    sample_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta property="og:url" content="https://www.allrecipes.com/sample" />
        <link rel="canonical" href="https://www.allrecipes.com/canonical" />
    </head>
    <body>
        <a href="https://www.allrecipes.com/link1">Link 1</a>
        <a href="https://www.allrecipes.com/link2">Link 2</a>
        <a href="https://www.hersheyland.com/link3">Link 3</a>
    </body>
    </html>
    """

    sample_soup = BeautifulSoup(sample_html, 'html.parser')
    return sample_soup


def test_concat_host_with_http_base_url_and_link(sample_soup):
    base_url = "http://www.example.com"
    link = "/recipes"
    expected_result = "http://www.example.com/recipes"
    assert concat_host(link, base_url, sample_soup) == expected_result

def test_concat_host_with_http_base_url_and_nonrelated_path(sample_soup):
    base_url = "http://www.example.com/about"
    link = "/recipes"
    expected_result = "http://www.example.com/recipes"
    assert concat_host(link, base_url, sample_soup) == expected_result

def test_concat_host_no_scheme_base_url_through_extract_base_domain(sample_soup):
    base_url = "www.allrecipes.com"
    link = "/recipes"
    expected_result = "https://www.allrecipes.com/recipes"
    assert concat_host(link, base_url, sample_soup) == expected_result

def test_concat_host_https_base_url(sample_soup):
    base_url = "https://www.example.com"
    link = "/recipes"
    expected_result = "https://www.example.com/recipes"
    assert concat_host(link, base_url, sample_soup) == expected_result

def test_concat_host_ext_base_url(sample_soup):
    base_url = ""
    link = "/recipes"
    expected_result = "https://www.allrecipes.com/recipes"
    assert concat_host(link, base_url, sample_soup) == expected_result

def test_concat_host_no_http_base_url(sample_soup):
    base_url = "ftp://www.allrecipes.com"
    link = "/recipes"
    expected_result = "https://www.allrecipes.com/recipes"
    assert concat_host(link, base_url, sample_soup) == expected_result

def test_concat_host_full_link(sample_soup):
    base_url = "http://example.com"
    link = "http://example.com/recipes"
    expected_result = "http://example.com/recipes"
    assert concat_host(link, base_url, sample_soup) == expected_result

def test_concat_host_invalid_url(sample_soup):
    base_url = "http://example.com"
    link = None
    with pytest.raises(TypeError):
        concat_host(link, base_url, sample_soup)

def test_concat_host_invalid_base_url(sample_soup):
    base_url = None
    link = "/recipes"
    expected_result = "https://www.allrecipes.com/recipes"
    assert concat_host(link, base_url, sample_soup) == expected_result