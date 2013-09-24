f = open("p13data.txt")
f.close

numbers = []
for line in f.readlines():
	number = []
	for c in line[:50]:
		number.append(int(c))
	numbers.append(number)

J = range(50)
J.reverse()
overflow = 0
backup = 0
answer = []

for j in J:
	v = overflow
	for i in range(100):
		v += numbers[i][j]
	v = str(v)
	answer.append(int(v[2]))
	overflow = int(v[1]) + backup
	if overflow >= 10:
		backup =  int(overflow/10)
		overflow = overflow % 10
	else:
		backup = 0
	backup += int(v[0])
answer.append(overflow)
answer.append(backup)
answer.reverse()
answer[:10]
answer_str = ""
for i in answer[:10]:
	answer_str = answer_str + str(i)


print answer

print answer_str