import httpx
from bs4 import BeautifulSoup
import re
import random
import time
# from datetime import datetime

def get_new_urls(random_sleeps=True, lower_sleep=2, upper_sleep=5):
    headers = {
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'sec-ch-ua': 'Google Chrome;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'sec-fetch-site': 'none',
        'sec-fetch-mod': '',
        'sec-fetch-user': '?1',
        'accept-encoding': 'gzip',
        'accept-language': 'en-US,en;q=0.9,de;q=0.5'
    }

    # List of base URLs with their corresponding patterns
    url_patterns = [
        ("https://www.allrecipes.com/recipes/22908/everyday-cooking/special-collections/new/", re.compile(r'https://www\.allrecipes\.com/recipe/\d+/\w+(?:-\w+)+/')),
        ("https://food52.com/recipes/newest", re.compile(r'/recipes/([^/]+)')),
        ("https://cooking.nytimes.com/68861692-nyt-cooking/32998034-our-newest-recipes", re.compile(r'/recipes/\d+-[a-z-]+')),
        ("https://www.hellofresh.com/recipes/most-recent-recipes", re.compile(r'https://www\.hellofresh\.com/recipes/[\d\w-]+-\w{24}')),
        ("http://www.afghankitchenrecipes.com/recent-recipes/", re.compile(r'http://www\.afghankitchenrecipes\.com/recipe/[\w-]+/')),
        ("https://www.baking-sense.com/all-blog-posts/", re.compile(r'https://www\.baking-sense\.com/\d+/\d+/\d+/[\w-]+/')), 
        ("https://www.bongeats.com/recipes", re.compile(r'/recipe/([\w-]+)'))
    ]

    concatenation_urls = {
        "https://food52.com/recipes/newest": "https://www.food52.com{}",
        "https://cooking.nytimes.com/68861692-nyt-cooking/32998034-our-newest-recipes": "https://cooking.nytimes.com{}", 
        "https://www.bongeats.com/recipes": "https://www.bongeats.com{}",
    }

    if random_sleeps:
        sleep_time = random.uniform(lower_sleep, upper_sleep)
        time.sleep(sleep_time)

    filtered_urls = []

    for base_url, pattern in url_patterns:
        html = httpx.get(url=base_url, headers=headers).content
        soup = BeautifulSoup(html, "html.parser")

        # Find all <a> tags with a 'href' attribute
        links = [a["href"] for a in soup.find_all("a", href=True)]

        # Apply pattern-based filtering
        recipe_links = [url if concatenation_urls.get(base_url) is None else concatenation_urls[base_url].format(url) for url in links if pattern.match(url)]

        # # Print relevant information for debugging
        # print(f"Base URL: {base_url}")
        # print(f"Concatenation URL: {concatenation_urls.get(base_url)}")
        # print(f"Filtered Recipe Links: {recipe_links}")

        # Add the filtered links to the result
        filtered_urls.extend(recipe_links)

    random.shuffle(filtered_urls)

    return filtered_urls

# Example usage
new_urls = get_new_urls()
print(len(new_urls))
print(new_urls)


# def get_new_urls(run_all=False, random_sleeps=True, lower_sleep=2, upper_sleep=5):
#     headers = {
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#         'sec-ch-ua': 'Google Chrome;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': 'Windows',
#         'sec-fetch-site': 'none',
#         'sec-fetch-mod': '',
#         'sec-fetch-user': '?1',
#         'accept-encoding': 'gzip',
#         'accept-language': 'en-US,en;q=0.9,de;q=0.5'
#     }

#     # List of base URLs with their corresponding patterns
#     daily_urls = [
#         ("https://food52.com/recipes/newest", re.compile(r'/recipes/([^/]+)')), 
#         ("https://cooking.nytimes.com/68861692-nyt-cooking/32998034-our-newest-recipes", re.compile(r'/recipes/\d+-[a-z-]+')), 
#         ("https://www.bongeats.com/recipes", re.compile(r'/recipe/([\w-]+)'))
#     ]

#     weekly_urls = [
#         ("https://www.hellofresh.com/recipes/most-recent-recipes", re.compile(r'https://www\.hellofresh\.com/recipes/[\d\w-]+-\w{24}')), 
#         ("https://www.baking-sense.com/all-blog-posts/", re.compile(r'https://www\.baking-sense\.com/\d+/\d+/\d+/[\w-]+/'))
#     ]

#     monthly_urls = [
    
#     ]

#     yearly_urls = [
#         ("https://www.allrecipes.com/recipes/22908/everyday-cooking/special-collections/new/", re.compile(r'https://www\.allrecipes\.com/recipe/\d+/\w+(?:-\w+)+/')),
#         ("http://www.afghankitchenrecipes.com/recent-recipes/", re.compile(r'http://www\.afghankitchenrecipes\.com/recipe/[\w-]+/'))
#     ]

#     concatenation_urls = {
#         "https://food52.com/recipes/newest": "https://www.food52.com{}",
#         "https://cooking.nytimes.com/68861692-nyt-cooking/32998034-our-newest-recipes": "https://cooking.nytimes.com{}", 
#         "https://www.bongeats.com/recipes": "https://www.bongeats.com{}",
#     }

#     if run_all:
#         update_urls = daily_urls + weekly_urls + monthly_urls + yearly_urls
#     else:
#         current_time = datetime.now()
#         current_day = current_time.day
#         current_week = current_time.isocalendar()[1]
#         current_month = current_time.month
#         current_year = current_time.year

#         update_urls = []

#         # Check if daily URLs should be updated
#         if current_time.hour == 0 and current_time.minute == 0 and current_time.second == 0:
#             update_urls.extend(daily_urls)

#         # Check if weekly URLs should be updated
#         if current_time.weekday() == 0 and current_time.hour == 0 and current_time.minute == 0 and current_time.second == 0:
#             update_urls.extend(weekly_urls)

#         # Check if monthly URLs should be updated
#         if current_day == 1 and current_time.hour == 0 and current_time.minute == 0 and current_time.second == 0:
#             update_urls.extend(monthly_urls)

#         # Check if yearly URLs should be updated
#         if current_day == 1 and current_month == 1 and current_time.hour == 0 and current_time.minute == 0 and current_time.second == 0:
#             update_urls.extend(yearly_urls)

#     if random_sleeps:
#         sleep_time = random.uniform(lower_sleep, upper_sleep)
#         time.sleep(sleep_time)

#     filtered_urls = []

#     for base_url, pattern in update_urls:
#         html = httpx.get(url=base_url, headers=headers).content
#         soup = BeautifulSoup(html, "html.parser")

#         # Find all <a> tags with a 'href' attribute
#         links = [a["href"] for a in soup.find_all("a", href=True)]

#         # Apply pattern-based filtering
#         recipe_links = [url if concatenation_urls.get(base_url) is None else concatenation_urls[base_url].format(url) for url in links if pattern.match(url)]

#         # Add the filtered links to the result
#         filtered_urls.extend(recipe_links)

#     random.shuffle(filtered_urls)

#     return filtered_urls
