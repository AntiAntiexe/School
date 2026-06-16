import requests
import time

for x in range(99, 101):
    repsonse = requests.get(f'https://api.jikan.moe/v4/anime/{x}')
    data = repsonse.json()

    score = data['data']['score']
    print(f'Anime ID: {x}, Score: {score}')

    
    time.sleep(1)  # To avoid hitting the rate limit of the API