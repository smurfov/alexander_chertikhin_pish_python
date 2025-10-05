# Решение Лабораторной работы №2

# Задача №1
print("Задача №1")

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