def main():
	longest_cycle = 0
	longest_cycle_number = 1
	for n in range(2,1000):
		print "testing number %d" % n
		k = 0
		non_cyclic = True
		while non_cyclic:
			# print "period %d" % k
			k += 1
			# non-cyclic number
			if pow(10, k) % n == 0:
				print "divisible by 1"
				break
			else:
				j = 0
				while j < k:
					trial_number = (pow(10, k-j) - 1) * pow(10, j) 
					# print "testing divisor %d " % trial_number
					if (trial_number % n) == 0:
						# print "number = %d has period %d" % (n, k-j)
						if k > longest_cycle:
							longest_cycle = k 
							longest_cycle_number = n
						non_cyclic = False
						break
					j += 1

	print longest_cycle_number
	print longest_cycle


def is_cyclic(n, k):
	if pow(10, k) % n == 0:
		return False
	if (pow(10, k) - 1) % n == 0:
		return True
	return True


if __name__ == "__main__":
    main()

