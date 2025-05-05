'''my_array = [12, 23, 19, 11, 1, 20, 342, 29]

LengthOne = len(my_array)

for i in range(LengthOne-1):
    min_index = 1

    for j in range(i+1, LengthOne):
        if my_array[i] < my_array[min_index]:
            min_index = j
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)

print(my_array)'''


my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)

print("Sorted array:", my_array)


