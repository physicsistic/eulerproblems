# Quadratic Primes

import utils as u

primes = u.erato_sieve(1000)
print primes

def f(a, b, n):
	return n * n + a * n + b

def is_prime(number):
	max_p = primes[-1]
	if number < max_p:
		for p in primes:
			if number == p:
				return True
			if number % p == 0:
				return False
		# return True
	else:
		# update the primes list
		n = max_p
		while n <= number:
			is_prime = True
			n += 1
			for p in primes:
				if n % p == 0:
					is_prime = False
					break

			if is_prime == True:
				primes.append(n)
		if primes[-1] == number:
			return True
		else:
			return False

bs = u.erato_sieve(1000)
max_n = 0
ideal_a = None
ideal_b = None
for b in bs:
	for a in range(-b, 1000):
		n = 0 
		while True:
			fn = f(a, b, n)
			if is_prime(fn) == True:
				n+=1
			else:
				break

		if n > max_n:
			max_n = n
			ideal_a = a
			ideal_b = b


print "a = %d, b = %d: a * b = %d" % (ideal_a, ideal_b, (ideal_a*ideal_b))


