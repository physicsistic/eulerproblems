def is_prime(number, primes):
	for prime in primes:
		if number % prime == 0:
			return False
	return True

number = 2
primes = [2]
position = 1
total_sum = 0

while number < 10:#pow(10,6)*2:
	if is_prime(number, primes) == True:
		primes.append(number)
		position += 1
		total_sum += number
		print("%dth prime number: %d" % (position, number))
	number += 1

print ("Sum of primes below 2 million = %d" % total_sum)