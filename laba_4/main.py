# Уникальные элементы
print("Задача №1")
sentence = "apple banana apple orange banana kiwi"
# Вывод: ['apple', 'banana', 'kiwi', 'orange']

words = set(sentence.split())

result = sorted(words)
print(result)

# Подсчёт частоты элементов
print("\nЗадача №2")
string = "abracadabra"
# Вывод: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

result = {}

for char in string:
	if char in result:
		result[char] += 1
	else:
		result[char] = 1

print(result)

# Пересечение списков
print("\nЗадача №3")

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
# Вывод: [4, 5]

set1 = set(list1)
set2 = set(list2)

result = set1 & set2
sorted_result = sorted(result)

print(sorted_result)

# Словарь квадратов
print("\nЗадача №4")

n = 5
# Вывод: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

result = {}

for i in range(1, n+1):
	result[i] = i**2

print(result)

# Проверка на анаграмму
print("\nЗадача №5")

string1 = "listen"
string2 = "silent"
# Вывод: True

if sorted(string1) == sorted(string2):
	print(True)
else:
	print(False)