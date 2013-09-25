# Names Scores #

f = open('names.txt', 'r')

start = ord('A') - 1 
name_score = 0

def score_name(n):
	return sum(map(lambda c: ord(c) - start, n))

names = map(lambda name: name[1:-1], f.read().split(','))
names.sort()

for i in range(len(names)):
	name_score += (i+1)*score_name(names[i])
	if names[i] == 'COLIN':
		print i+1
		print score_name('COLIN')

print name_score