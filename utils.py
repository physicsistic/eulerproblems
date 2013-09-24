#!/usr/bin/env

def factorize(number):
	factors = []
	factor = 2 
	while factor <= number:
		while number % factor == 0:
			number = number / factor
			factors.append(factor)
		factor += 1
	return factors
