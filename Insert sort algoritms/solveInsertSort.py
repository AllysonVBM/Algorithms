def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

test_array = [12, 11, 13, 5, 6]
sorted_array = insertion_sort(test_array)
print(sorted_array)
