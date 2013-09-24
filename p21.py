# Amicable Numbers #

from math import sqrt

def factorize(number):
	factors = [1]
	for i in range(2, int(sqrt(number))+1):
		if number%i == 0:
			if number/i != i:
				factors.append(i)
				factors.append(number/i)
			else:
				factors.append(i)
	return factors
# for i in range(65):
# 	print i
# 	print factorize(i)

max_number = 10000
all_numbers = range(1,max_number)
amicable_sum = 0

for n in all_numbers:
	n_factors = factorize(n)
	a = sum(n_factors)
	a_factors = factorize(a)
	if sum(a_factors) == n:
		if a < max_number:
			all_numbers.remove(a)
		print "the amicable pair is (%d, %d)" % (a, n)
		if a != n:
			amicable_sum += a
			amicable_sum += n
	
print amicable_sum