import math

# Решение Лабораторной работы №3

# Задача №1
# Циклический сдвиг массива
print("Задача №1")
array = [0, 0, 0, 0, 0]
for i in range(5):
	array[i] = int(input(f"Введите число в массив под №{i}: "))

shift = int(input("Введите ваш сдвиг: "))

shifted = array[-shift:] + array[:-shift]

print(shifted)

# Задача №2
# Перестановка вложенных списков

print("\nЗадача №2")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
shift = int(input("Введите ваш сдвиг: "))

result = []
for row in matrix:
	shifted_row = row[-shift:] + row[:-shift]
	result.append(shifted_row)

for row in result:
    print(row)

# Задача №3
# Разворот блоков в списке

print("\nЗадача №3")
array = [1, 2, 3, 4, 5, 6, 7]
block_size = int(input("Введите размер блока: "))
result = []



for i in range(math.ceil(len(array) / block_size)):
	copied = array[(block_size * i):(block_size * (i + 1))]
	copied = copied[::-1]
	result += copied

print(result)

# Задача №4
# Поиск максимальной суммы подмассива фиксированной длины

print("\nЗадача №4")
array = [1, -2, 3, 4, -1, 2, 1, -5, 4]
k = int(input("Введите размер модмассива: "))

current_sum = sum(array[:k])
max_sum = current_sum
max_start = 0

for i in range(1, len(array) - k + 1):
    current_sum = current_sum - array[i-1] + array[i+k-1]
    if current_sum > max_sum:
        max_sum = current_sum
        max_start = i

result = array[max_start:max_start + k]
print(result)
print(f"Сумма: {max_sum}")