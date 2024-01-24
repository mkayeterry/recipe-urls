from typing import Optional

def categorize_url(base_url: str) -> Optional[str]:
    site_origins = [
        'abuelascounter', 
        'acouplecooks', 
        'addapinch', 
        'afghankitchenrecipes', 
        'allrecipes', 
        'averiecooks',
        'baking-sense',
        'bongeats',
        'food52',
        'food',
        'hellofresh',
        'nytimes'
    ]

    for site_origin in site_origins:
            try:
                if site_origin in base_url:
                    print(f"[utils.py] {base_url} successfully categorized as {site_origin}.")
                    return site_origin

            except Exception as e:
                print(f"[utils.py] Error: An unexpected error occurred - {e}")
                raise  # Re-raise the exception

    # If none of the site origins are found, print a warning
    print(f"[utils.py] Warning: Unable to categorize URL '{base_url}'.")
