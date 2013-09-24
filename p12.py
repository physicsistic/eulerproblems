number = 4
primes = [2,3,5]

def count_divisors(number):
	divisors = dict()
	i = 0
	while i < len(primes):
		p = primes[i]
		# check whether to update prime list
		l = len(primes)
		if i + 1 == l:
			while (len(primes) - l) < 5:
				is_prime = True
				for prime in primes:
					if p % prime == 0:
						is_prime = False
						break
				if is_prime == True:
					primes.append(p)
				else:
					p += 1

		if p > number:
			num_divisors = 1
			# calculate number of divisors
			for k, v in divisors.items():
				num_divisors = num_divisors * (v + 1)

			if num_divisors == 1:
				num_divisors += 1
			return num_divisors

		while number % p == 0:
			number = number / p
			if p in divisors.keys():
				divisors[p] += 1
			else:
				divisors[p] = 1
		i += 1

d_n1 = 4
d_max = 2
not_found = True
while not_found:
	d_n = d_n1
	number += 1
	T_n = number*(number+1)/2
	d_Tn = count_divisors(T_n)
	print("%d:\tT_n=%d, d_Tn=%d" % (number-1, T_n, d_Tn))

	if d_Tn > 500:
		not_found = False
		print "Tn = %d has %d divisors" % (T_n, d_Tn)

