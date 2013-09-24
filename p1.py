# Multiples of 3 and 5

total_sum = 0
for i in range(1,100):
	if i % 3 == 0 or i % 5 == 0:
		total_sum += i

print total_sum