from typing import Optional

def get_site_origin(base_url: str) -> Optional[str]:
    site_origins = [
        'abuelascounter', 
        'acouplecooks', 
        'addapinch', 
        'afghankitchenrecipes', 
        'allrecipes', 
        'ambitiouskitchen', 
        'archanaskitchen', 
        'averiecooks',
        'bakingmischief',
        'baking-sense',
        'barefootcontessa',
        'bbc',  
        'bettycrocker', 
        'bigoven', 
        'bluejeanchef', 
        'bonappetit', 
        'bongeats',
        'bowlofdelicious', 
        'budgetbytes', 
        'carlsbadcravings', 
        'castironketo', 
        'cdkitchen', 
        'chefsavvy', 
        'closetcooking', 
        'cookieandkate',
        'copykat', 
        'countryliving',
        'creativecanning',  
        'davidlebovitz', 
        'delish', 
        'domesticate-me', 
        'downshiftology', 
        'eatingbirdfood', 
        'eatingwell', 
        'eatliverun', 
        'eatsmarter', 
        'eatwell101', 
        'eatwhattonight', 
        'elavegan', 
        'ethanchlebowski', 
        'epicurious', 
        'food52',
        'food',
        'hellofresh',
        'ninjatestkitchen', 
        'nytimes'
    ]

    for site_origin in site_origins:
        if site_origin in base_url:
            return site_origin

    raise ValueError(f"URL '{base_url}' is not supported.")