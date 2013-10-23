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

def erato_sieve(n):
	nums = [True] * (n+1)
	prime_nums = []
	p = 2
	while p <= n:
		if nums[p] == False:
			p += 1
		else:
			prime_nums.append(p)
			pp = p * 2
			while pp <= n:
				nums[pp] = False
				pp += p
			p += 1

	return prime_nums

def erato_sieve_extend(primes, dn):
	return None
