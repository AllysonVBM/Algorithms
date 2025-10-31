numbers = [7, 3, 6, 2, 0]
size = len(numbers)
for i in range(size -1): 
    for j in range (size -i -1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)