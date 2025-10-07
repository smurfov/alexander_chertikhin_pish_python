# Решение Лабораторной работы №2

# Задача №1
print("Задача №1")
x = int(input("Введи число x: "))

def f1(x):
    # Вычисляет x^2 для x в диапазоне [-2, 2)
    return x ** 2

def f2(x):
    # Вычисляет x² + 4x + 5 для x >= 2
    return x ** 2 + 4 * x + 5

def f3(x):
    # Возвращает 4 для x < -2
    return 4

# Основная функция, которая выбирает нужную
def f(x):
    if -2 <= x < 2:
        return f1(x)
    elif x >= 2:
        return f2(x)
    else:  # x < -2
        return f3(x)

print(f"Значение функции f(x) = {f(x)}")

# Задача №2
# Составить функцию, которая определяет наибольший общий делитель двух чисел nod(a, b)
print("\nЗадача №2")
a = int(input("Введите число а: "))
b = int(input("Введите число b: "))

def NOD(a, b):
	while b != 0:
		a, b = b, a % b
	return a

print("НОД(", a, ",", b, ") =", NOD(a, b))


# Задача №3
# Составить логическую функцию, которая определяет, верно ли, что в заданном числе сумма цифр равна произведению

print("\nЗадача №3")
number = int(input("Введите ваше число: "))

def check(number):
	equal = 1
	sum = 0
	while number > 0:
		a = number % 10
		number //= 10
		sum += a
		equal *= a
	if sum != equal:
		return False
	else:
		return True

if check(number):
	print("Сумма цифр равна произведению!")
else:
	print("Сумма цифра не равна произведению!")


# Задача №4
# Составить функцию, которая определяет сумму цифр в числе
print("\nЗадача №4")
number = int(input("Введите ваше число: "))

def sumOfNumber(number):
	sum = 0
	while number > 0:
		a = number % 10
		number //= 10
		sum += a
	return sum

sum = sumOfNumber(number)
print("Сумма цифр в числе", number, "=", sum)