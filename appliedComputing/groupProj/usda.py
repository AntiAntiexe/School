import requests

USDA_API_KEY = '########################'

def search_food(food_name):
    url = 'https://api.nal.usda.gov/fdc/v1/foods/search'
    params = {
        'api_key': USDA_API_KEY,
        'query': food_name,
        'pageSize': 1  # get top result only
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data['foods']:
        return data['foods'][0]['fdcId']
    return None
def get_nutrition(fdc_id):
    url = f'https://api.nal.usda.gov/fdc/v1/food/{fdc_id}'
    params = {'api_key': USDA_API_KEY}
    response = requests.get(url, params=params)
    data = response.json()

    # Extract nutrients we care about (calories, fat, carbs, protein, fiber)
    nutrients = {
        "Calories": None,
        "Fat": None,
        "Carbohydrates": None,
        "Protein": None,
        "Fiber": None
    }

    nutrient_map = {
        208: "Calories",        # Energy kcal
        204: "Fat",             # Total lipid (fat)
        205: "Carbohydrates",   # Carbohydrate, by difference
        203: "Protein",         # Protein
        291: "Fiber"            # Fiber, total dietary
    }

    for nutrient in data.get('foodNutrients', []):
        nutrient_id = nutrient.get('nutrient', {}).get('id') or nutrient.get('nutrientId')
        if nutrient_id in nutrient_map:
            name = nutrient_map[nutrient_id]
            value = nutrient.get('amount')
            unit = nutrient.get('nutrient', {}).get('unitName') or nutrient.get('unitName')
            nutrients[name] = f"{value} {unit}"

    return nutrients

if __name__ == "__main__":
    food = input("Enter a fruit or vegetable name: ")
    fdc_id = search_food(food)
    if fdc_id:
        nutrition = get_nutrition(fdc_id)
        print(f"Nutritional info for {food.capitalize()} (per 100g):")
        for k, v in nutrition.items():
            print(f"{k}: {v}")
    else:
        print("Food item not found.")