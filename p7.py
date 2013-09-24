import time
def is_prime_slow(number):
	factor = 2
	while factor < number:
		if number % factor == 0:
			return False
		factor += 1
	return True

def is_prime_faster(number, primes):
	for prime in primes:
		if number % prime == 0:
			return False
	return True

position = 1
number = 2
primes = [2]

start = time.clock()
while position != 10001:
	if is_prime_faster(number, primes) == True:
		primes.append(number)
		position += 1
		print("%dth prime number: %d" % (position, number))
	number += 1
print("time elapsed %f" % (time.clock()-start))