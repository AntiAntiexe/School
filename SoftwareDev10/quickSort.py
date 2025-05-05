numbers = [8, 2, 5, 3, 9, 4, 7, 6, 1]

def quickSort(array, start, end):

    

    pivot = partition(array, start, end)
    quickSort(array, start, pivot-1)
    quickSort(array, pivot+1, end)

    if end <= start:
        return array 

def partition(array, start, end):

    pivot = array[end]
    i = start-1
    j = start
    while j <= end-1:
        if array[j] < pivot:
            i = i+1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
        j = j+1
    
    i = i+1
    temp = array[i]
    array[i] = array[end]
    array[end] = temp


    return i



print(quickSort(numbers, 0, len(numbers)-1))