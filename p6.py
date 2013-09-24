numbers = range(1, 101)
difference = 0


for i in numbers:
	for j in numbers:
		if i != j:
			difference += i*j

print difference