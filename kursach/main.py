from data_functions import *
from console_functions import *
from math_functions import *

def main():
	parser = initParser()
	args = parser.parse_args()
	data = readFileAndSaveContent(args.file, args.read)
	if data is None:
		return
	else:
		data = add_random_invalid_values_probability(data)
		data = formattedData(data)

		if args.month:
			operation_for_month(data, args.month)

		if args.year:
			operation_for_year(data)

if __name__ == '__main__':
	main()
