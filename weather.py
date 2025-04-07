import requests

# API endpoint and key
API_URL = "https://api.weatherbit.io/v2.0/current"
API_KEY = "1751e3ea46d74778b8810b4ecd5ade88"

# Parameters for the API request
params = {
    "country": "au",
    "apiKey": API_KEY,
    "units": "M"
}

# Making the API request
response = requests.get(API_URL, params=params)

# Checking if the request was successful
if response.status_code == 200:
    # Printing the JSON response
    print(response.json())
else:
    print(f"Error: {response.status_code}")
