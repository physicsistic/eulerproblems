# 1000-digit Fibonacci number #

Fn = 1
Fn1 = 1
n = 1


max_F = pow(10,999)

while Fn < max_F:
	new_F = Fn + Fn1
	Fn = Fn1
	Fn1 = new_F
	n += 1

print Fn
print n

