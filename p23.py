# Non-abundant sums #

from math import sqrt

max_number = 28124

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
	
abundant_numbers = []

for i in range(1, max_number):
	if sum(factorize(i)) > i:
		abundant_numbers.append(i)

L = len(abundant_numbers)

all_numbers = set(range(1,max_number))

for i in range(L):
	for j in range(i,L):
		x = abundant_numbers[i] + abundant_numbers[j]
		if x in all_numbers:
			all_numbers.remove(x)

print sum(all_numbers)
