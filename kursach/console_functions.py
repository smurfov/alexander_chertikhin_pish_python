import argparse

def initParser():
	parser = argparse.ArgumentParser(description="Чтение команд с консоли")

	parser.add_argument("-f", "--file", type=str, help="Название файла")
	parser.add_argument("-r", "--read", action="store_true", help="Чтение файла")
	parser.add_argument("-m", "--month", type=int, help="Расчет за месяца")
	parser.add_argument("-y", "--year", action="store_true", help="Расчет за год")

	return parser