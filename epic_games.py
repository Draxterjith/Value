import requests

url = 'https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=US&allowCountries=US'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for game in data['data']['Catalog']['searchStore']['elements']:
        if game['promotions'] and game['promotions']['promotionalOffers']:
            # The game is currently free
            title = game['title']
            description = game['description']
            thumbnail = game['keyImages'][0]['url']
            print(f"{title} is currently free on the Epic Games Store!")
else:
    print("Error retrieving data from Epic Games Store API")
