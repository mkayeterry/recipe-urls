import pytest
from urllib.parse import urlparse
from recipe_urls._utils import SITE_ORIGINS, get_site_origin, extract_base_domain


# Expanded parameterized tests for error cases
@pytest.mark.parametrize("url, expected_exception", [
    ("", "Either base_url or html must be provided."),
    ("https://example.com", "URL 'https://example.com' is not supported."),
    (None, "Either base_url or html must be provided."),
    (123, "URL is not a valid format"),
    ("invalid_url", "URL is not a valid format"),
    (["https://example.com"], "URL is not a valid format"),
    ({"url": "https://example.com"}, "URL is not a valid format"),
    ("http://☕.com", "URL is not a valid format"),
    ("https://user:pass@domain.com", "URL 'https://user:pass@domain.com' is not supported."),
    ("https://example.com/<script>alert('xss')</script>", "URL 'https://example.com/<script>alert('xss')</script>' is not supported."),
    ("https://very-long-url-" + "a" * 25 + ".com", "URL 'https://very-long-url-" + "a" * 25 + ".com' is not supported."),
    ("ftp://example.com", "URL is not a valid format"),
    ("sftp://example.com", "URL is not a valid format"),
    ("mailto:test@example.com", "URL is not a valid format"),
    ("data:text/plain;base64,SGVsbG8sIFdvcmxkIQ%3D%3D", "URL is not a valid format"),
    ("file:///path/to/file.txt", "URL is not a valid format"),
    ("about:blank", "URL is not a valid format"),
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
    domain = parsed_url.hostname
    normalized_domain = extract_base_domain(domain)
    assert get_site_origin(url) == normalized_domain, f"ValueError: URL '{normalized_domain}' is not supported."