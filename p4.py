# -----
# Largest palindrome product
# -----
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 * 99.
from itertools import combinations

def check_palindrome(number):
	num_str = str(number)
	num_str_len = len(num_str)
	for i in range(num_str_len/2):
		if num_str[i] != num_str[num_str_len-i-1]:
			return False
	return True
	
def factorize(number):
	factors = []
	factor = 2 
	while factor <= number:
		while number % factor == 0:
			number = number / factor
			factors.append(factor)
		factor += 1
	return factors

nums = range(1,10)
digits = range(10)
# nums.reverse()
# digits.reverse()
largest_palindrome = 0

for a in nums:
	for b in digits:
		for c in digits:
			palindrome = int(str(a)+str(b)+str(c)+str(c)+str(b)+str(a))
			factors = factorize(palindrome)
			for i in range(1, len(factors)):
				partitions = combinations(factors, i)
				for partition in partitions:
					print partition
					factor = 1
					for x in partition:
						factor = factor * x
					if len(str(factor)) == 3 & len(str(palindrome/factor)) == 3:
						if palindrome > largest_palindrome:
							largest_palindrome = palindrome
						print "found palindrome %d with factors (%d,%d)" % (palindrome, factor, palindrome/factor)

print "largest palindrome = %d " % largest_palindrome