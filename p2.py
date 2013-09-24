i, j = 1, 2
limit = pow(10, 6) * 4
total = 0
while j < limit:
	if j % 2 == 0:
		total += j
	old_j = j
	j = i + old_j
	i = old_j

print total