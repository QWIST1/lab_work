numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
searh_none = numbers[:4] + numbers[5:]
none = sum(searh_none)/len(numbers)
numbers[4] = none
print("Измененный список:", numbers)
