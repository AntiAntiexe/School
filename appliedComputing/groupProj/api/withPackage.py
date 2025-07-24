import fooddatacentral as fdc
import pandas as pd

apikey = "ut3YgGsXJZZF0KDSHYbnX5j4Xo4PmmBhpGIYQneO"


#print(fdc.search(apikey,"pear"))




nutrientData = fdc.nutrients(apikey,fdc_id=fdcIds["pear"])

print('Data: ', nutrientData.head())  # Print Protein nutrient
#print(nutrientData.iloc[0, 1, 2, 3, 5, 8, 9, 10, 11, 12, 13, 14, 15, 20, 23, 24, 28, 32, 34])  # Print Protein nutrient
#print(nutrientData.to_string())

#print(nutrientData.iloc[1])  # Print Protein nutrient

#nutrients = []

#for i in range(len(nutrientData)):
  #  nutrients.append(nutrientData.iloc[i])

#for i in range(len(nutrientData.index)):
    #nutrients.append(nutrientData.iloc[i])
    #print(i)
    
#print(nutrients)

#print(nutrientData.drop())


class NutrientData:
    def __init__(self):
        self.fdcIds = {
          "apple": 2709223,
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
          "muskmelon":  169134
        }

        self.apikey = "ut3YgGsXJZZF0KDSHYbnX5j4Xo4PmmBhpGIYQneO"

    def get_nutrient_data(self, fruit_name):
        if fruit_name in self.fdcIds:
            fdc_id = self.fdcIds[fruit_name]
            nutrientData = fdc.nutrients(self.apikey, fdc_id=fdc_id)
            return nutrientData