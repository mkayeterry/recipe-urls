import pytest
from urllib.parse import urlparse
from recipe_urls._utils import SITE_ORIGINS, get_site_origin, extract_base_domain


# Expanded parameterized tests for error cases
@pytest.mark.parametrize("url, expected_exception", [
    ("", "Either base_url or html must be provided."),
    ("https://example.com", "URL not supported."),
    (None, "Either base_url or html must be provided."),
    (123, "URL format must be of type string."),
    ("invalid_url", "URL is not a valid format."),
    (["https://example.com"], "URL format must be of type string."),
    ({"url": "https://example.com"}, "URL format must be of type string."),
    ("http://☕.com", "URL not supported."),
    ("https://user:pass@domain.com", "URL not supported."),
    ("https://very-long-url-" + "a" * 25 + ".com", "URL not supported."),
    ("ftp://example.com", "URL scheme must be 'https' or 'http'."),
    ("sftp://example.com", "URL scheme must be 'https' or 'http'."),
    ("mailto:test@example.com", "URL is not a valid format."),
    ("data:text/plain;base64,SGVsbG8sIFdvcmxkIQ%3D%3D", "URL is not a valid format."),
    ("file:///path/to/file.txt", "URL is not a valid format."),
    ("about:blank", "URL is not a valid format.")
])


def test_get_site_origin_errors(url, expected_exception):

    with pytest.raises(ValueError) as e:
        get_site_origin(url)

    assert str(e.value) == expected_exception

@pytest.mark.parametrize("url", [
    f"https://{domain}" for domain in SITE_ORIGINS
])


def test_get_site_origin_success(url):

    parsed_url = urlparse(url)
    domain = parsed_url.hostname if not None else parsed_url.netloc
    normalized_domain = domain.lower()

    assert get_site_origin(url) == normalized_domain, f"ValueError: URL '{normalized_domain}' is not supported."