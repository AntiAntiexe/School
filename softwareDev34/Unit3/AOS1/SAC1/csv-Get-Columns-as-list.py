import csv

data = []
with open('softwareDev34/Unit3/AOS1/binarySearch/numbers.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

arr = [c[0] for c in data]

print(data)
print(arr)