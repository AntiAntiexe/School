import requests

API_KEY = 'Kxz6wxPEYehy7vtXbkGCzi1an30LnnEf'

url = 'https://api.deepinfra.com/v1/inference/meta-llama/Meta-Llama-3-8B-Instruct'

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
}

# Example: user asks about "avocado"
payload = {
    "input": "Provide nutritional facts for 100 grams of apple in this exact format:\nCalories: __\nFat: __g\nCarbohydrates: __g\nProtein: __g\nFiber: __g\nOnly output the facts, no explanation.",
    "parameters": {
        "max_new_tokens": 40,
        "temperature": 0,
    }
}


response = requests.post(url, headers=headers, json=payload)
result = response.json()

# Print result
print(result['results'][0]['generated_text'])

