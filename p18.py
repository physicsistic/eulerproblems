f = open("triangle.txt")
lines = f.readlines()
f.close()

pos = 0
N = []

for line in lines:
	numbers = map(int, line.split())
	N.append(numbers)

n = len(lines)

L = range(n-1)
L.reverse()
T = N[n-1]

for l in L:
	I = range(len(T)-1)
	Tn = []
	for i in I:
		if T[i] > T[i+1]:
			Tn.append(N[l][i] + T[i])
		else:
			Tn.append(N[l][i] + T[i+1])
	T = Tn

print T






