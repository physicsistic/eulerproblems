factor = 2
number = 600851475143

while factor < number:
	while number % factor == 0:
		number = number / factor
	factor += 1
	print number