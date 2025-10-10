from data_functions import renameMonth

def operation_for_month(data, month):
	if month > 12 or month < 1:
		print("Не существует такого месяца.")
		return None

	sum = 0
	count = 0
	min = 0
	max = 0
	for element in data:
		if element["month"] == month:
			sum += element["temperature"]
			if element["temperature"] > max:
				max = element["temperature"]
			if element["temperature"] < min:
				min = element["temperature"]
			count += 1
	
	middle = round(sum / count, 2)

	print(f"""
Результат за {renameMonth(month)} месяц:
Минимальное значение за месяц: {min}
Максимальное значение за месяц: {max}
Среднее значение за месяц: {middle}
""")


def operation_for_year(data):
	sum = 0
	count = 0
	min = 0
	max = 0
	year = data[0]["year"]
	for element in data:
		sum += element["temperature"]
		if element["temperature"] > max:
			max = element["temperature"]
		if element["temperature"] < min:
			min = element["temperature"]
		count += 1
	
	middle = round(sum / count, 2)

	print(f"""
Результат за {year}г.:
Минимальное значение за месяц: {min}
Максимальное значение за месяц: {max}
Среднее значение за месяц: {middle}
""")