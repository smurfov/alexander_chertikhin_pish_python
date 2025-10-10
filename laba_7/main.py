# Задание 1 Возведение чисел в квадрат
print("Задание №1")

numbers = [1, 2, 3, 4, 5]
# Ожидаемый результат: [1, 4, 9, 16, 25]

result = list(map(lambda x: x**2, numbers))
print(result)

# Задание 2 Фильтрация чётных чисел
print("\nЗадание №2")

numbers = [10, 15, 20, 25, 30]
# Ожидаемый результат: [10, 20, 30]

result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

# Задание 3 Сортировка списка слов по длине
print("\nЗадание №3")

words = ["apple", "banana", "pear", "grape", "kiwi"]
# Ожидаемый результат: ["kiwi", "pear", "apple", "grape", "banana"]

result = list(sorted(words, key=lambda x: len(x)))
print(result)

# Задание 4 Произведение всех чисел в списке
print("\nЗадание №4")

from functools import reduce

numbers = [1, 2, 3, 4]
# Ожидаемый результат: 24

result = reduce(lambda x, y: x * y, numbers)
print(result)

# Задание 5 Проверка на палиндромы
print("\nЗадание №5")

words = ["level", "world", "radar", "python", "madam"]
# Ожидаемый результат: ["level", "radar", "madam"]

result = list(filter(lambda x: x == x[::-1], words))
print(result)