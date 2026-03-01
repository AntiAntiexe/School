import csv


data = []
with open('softwareDev34/Unit3/AOS1/2DArrays/marks.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
print(data)