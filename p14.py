z = dict()


##### ATTEMPT 1 #######

# def find_chain_length(n):
# 	if n in z.keys():
# 		return z[n] 
# 	else:
# 		if n == 1:
# 			z[1] = 0
# 			return z[1]
# 		else:
# 			if n % 2 == 0:
# 				new_n = n / 2
# 			else:
# 				new_n = n * 3 + 1
# 			z[n] = find_chain_length(new_n) + 1
# 			return z[n]

# cap = pow(10,6)
# I = range(1, cap)
# I.reverse()

# for i in I:
# 	print i
# 	if len(z.keys()) >= cap:
# 		break
# 	find_chain_length(i)


# max_chain = 0
# answer = 0

# for k, v in z.items():
# 	if v > max_chain:
# 		max_chain = v
# 		answer = k
z[1] = 0
z[2] = 1
z[4] = 2
z[8] = 3

##### ATTEMPT 2 #######

# def collatz_split(n, d):
# 	z[n] = d
# 	l = len(z.keys())
# 	print l

# 	if l < pow(10,6):
# 		collatz_split(n*2, d + 1)
# 		if (n-1)%3 == 0:
# 			collatz_split((n-1)/3, d + 1)

# collatz_split(16, 4)

# for k, v in z.items():
# 	if v > max_chain:
# 		max_chain = v
# 		answer = k

# print "answer"
# print max_chain
# print answer

##### ATTEMPT 3 #######

# N = pow(10,6)
# longest_chain = 1

# def collatz_reduce(n):
# 	d = 0 
# 	old_n = n
# 	while n not in z.keys():
# 		if n % 2 == 0:
# 			n = n / 2
# 		else:
# 			n = n * 3 + 1
# 		d += 1

# 	z[old_n] = d + z[n]

# for i in range(1, N):
# 	collatz_reduce(i)
# 	if z[i] > longest_chain:
# 		longest_chain = i

# print "longest chain number = " + str(longest_chain) + " -> chain length = " + str(z[i])
# 	# find collatz

#### ATTEMPT 4 #######

N = pow(10,6)
longest = 1
answer = 2

for i in range(2, N):
	length = 0 
	n = i 
	while n != 1:
		length += 1
		if n % 2 == 0:
			n = n / 2
		else:
			n = n * 3 + 1
	if length > longest:
		longest = length
		answer = i
	if i % 100 == 0:
		print i






print "longest chain number = " + str(answer) + " -> chain length = " + str(longest)
	# find collatz






