import fooddatacentral as fdc
import pandas as pd

apikey = "ut3YgGsXJZZF0KDSHYbnX5j4Xo4PmmBhpGIYQneO"


#print(fdc.search(apikey,"avocado"))

id = 2709223    # Put an FDC ID HERE!
nutrientData = fdc.nutrients(apikey,fdc_id=id)

#print(nutrientData.head())  # Print Protein nutrient
#print(nutrientData.iloc[0, 1, 2, 3, 5, 8, 9, 10, 11, 12, 13, 14, 15, 20, 23, 24, 28, 32, 34])  # Print Protein nutrient
#print(nutrientData.to_string())

#print(nutrientData.iloc[1])  # Print Protein nutrient

nutrients = []

#for i in range(len(nutrientData)):
  #  nutrients.append(nutrientData.iloc[i])

for i in range(len(nutrientData.index)):
    nutrients.append(nutrientData.iloc[i])
    print(i)
    

#print(nutrients)

#print(nutrientData.drop())