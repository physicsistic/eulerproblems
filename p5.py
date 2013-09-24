factors = dict()
answer = 1

def factorize(number):
	factors = dict()
	factor = 2
	while factor <= number:
		while number % factor == 0:
			number = number / factor
			if factor in factors.keys():
				factors[factor] += 1
			else:
				factors[factor] = 1
		factor += 1
	print factors
	return factors

for i in range(2,21):	
	for factor, count in factorize(i).items():
		if factor in factors.keys():
			if count > factors[factor]:
				factors[factor] = count
		else:
			factors[factor] = count

	print "overall factor counts"
	print factors

for factor, count in factors.items():
	for _ in range(count):
		answer = answer * factor


print "final answer"
print(answer)