import random

def readFileAndSaveContent(name, is_read):
	if not name: 
		print("Вы не ввели название файла.")
		return None
	if not is_read:
		print("Файл не был прочитан.")
		return None

	with open(name, "r") as file:
		content = file.readlines()
		return content

def formattedData(array):
	result = []
	for element in array:
		cleaned = element.replace("\n", "").strip()
		splitted = cleaned.split(";")
		
		if splitted[5] == "-xx":
			continue

		dict = {
			"year": int(splitted[0]),
			"month": int(splitted[1]),
			"day": int(splitted[2]),
			"hour": int(splitted[3]),
			"minute": int(splitted[4]),
			"temperature": int(splitted[5]),
		}

		result.append(dict)
	return result

def add_random_invalid_values_probability(data, probability=0.4):
	result = []
	for element in data:
		if random.random() < probability:
			splitted = element.split(";")
			splitted[5] = "-xx"
			element = ";".join(splitted)
		result.append(element)
	return result


def renameMonth(number):
	monthsNames = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

	return monthsNames[number-1]