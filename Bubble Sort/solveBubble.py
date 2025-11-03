def bubble_sort(v):
    n = len(v)
    for i in range(n):
        for j in range(0, n - i - 1):
            if v[j] > v[j + 1]:
                temp = v[j]
                v[j] = v[j + 1]
                v[j + 1] = temp

v = [5, 2, 9, 1, 5, 6]
bubble_sort(v)
print(v)
