def NOD(a, b):
	while b != 0:
		a, b = b, a % b
	return a

def orderNumbers(number):
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
	
def sumOfNumber(number):
	sum = 0
	while number > 0:
		a = number % 10
		number //= 10
		sum += a
	return sum