numbers = [1, 2, 3, 4, 5, 6]
numbers[0], numbers[1] = numbers[1], numbers[0]
numbers[2], numbers[3] = numbers[3], numbers[2]
numbers[4], numbers[5] = numbers[5], numbers[4]
print(numbers)