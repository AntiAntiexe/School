import fooddatacentral as fdc
import pandas as pd


class NutrientData:
    def __init__(self):
        self.fdcIds = {
          "apple": 1750342  ,
          "banana": 1105314,
          "carambola": 171715,
          "guava": 173044,
          "kiwi": 63126500,
          "orange": 746771,
          "peach": 325430,
          "pear": 2710836,
          "persimmon": 169943,
          "plum": 169949,
          "pomegranate": 169134,
          "tomatoes": 169134,
          "muskmelon":  169134,
          "pineapple": 2346398,
          "mango": 2710834,
        }

        self.apikey = "ut3YgGsXJZZF0KDSHYbnX5j4Xo4PmmBhpGIYQneO"

    def getNutrientData(self, fruit_name):
        if fruit_name.lower() in self.fdcIds:
            fdc_id = self.fdcIds[fruit_name.lower()]
            nutrientData = fdc.nutrients(self.apikey, fdc_id=fdc_id)

            energy = nutrientData.loc["Energy (Atwater General Factors)"]
            carbohydrate = nutrientData.loc["Carbohydrate, by difference"]
            sugars = nutrientData.loc["Sugars, Total"]
            protein = nutrientData.loc["Protein"]
            total_lipid = nutrientData.loc["Total lipid (fat)"]

            return energy, carbohydrate, sugars, protein, total_lipid
