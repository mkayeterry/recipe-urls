from recipe_urls.utils import categorize_url

def get_recipe_urls(base_urls):

    if not isinstance(base_urls, list):
        base_urls = [base_urls]

    for base_url in base_urls:
        class_name = categorize_url(base_url)
        if class_name:
            # Dynamically import the class based on its name
            scraper_class = globals()[class_name]
            
            # Create an instance and call the scrape method
            scraper_instance = scraper_class(base_url)
            scraper_instance.scrape()
        else:
            print(f"URL '{base_url}' not recognized.")