#!/usr/bin/env

# def factorize(number):
# 	factors = []
# 	factor = 2 
# 	while factor <= number:
# 		while number % factor == 0:
# 			number = number / factor
# 			factors.append(factor)
# 		factor += 1
# 	return factors


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

def find_prime(max_number):
	