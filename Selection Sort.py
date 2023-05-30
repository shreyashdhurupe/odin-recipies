def selection_sort(array,size):
    for i in range(size):
        min_index = i

        for j in range(i+1,size):
            if array[j] < array[min_index]:
                min_index = j

        (array[i], array[min_index]) = (array[min_index], array[i])

data = [1,0,66,84,12]
size = len(data)
selection_sort(data,size)
print(data)