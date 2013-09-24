MAX = 1000
total = 0

z = {
	0: '', 
	1: 'one', 
	2: 'two', 
	3: 'three', 
	4: 'four', 
	5: 'five', 
	6: 'six', 
	7: 'seven', 
	8: 'eight', 
	9: 'nine',
	11: 'eleven', 
	12: 'twelve', 
	13: 'thirteen', 
	14: 'fourteen', 
	15: 'fifteen', 
	16: 'sixteen', 
	17: 'seventeen', 
	18: 'eighteen', 
	19: 'nineteen', 
	20: 'twenty',
	10: 'ten', 
	20: 'twenty', 
	30: 'thirty', 
	40: 'forty', 
	50: 'fifty', 
	60: 'sixty', 
	70: 'seventy', 
	80: 'eighty', 
	90: 'ninety',
	100: 'one hundred',
	1000: 'one thousand'
	}
for i in range(1, 1001):
	s = ''
	if i in z:
		s = z[i]
	else:
		if i < 100:
			s = z[i/10*10] + '-' + z[i%10]
			z[i] = s
		else:
			r = i % 100
			if r == 0:
				s = z[i/100] + ' hundred'
			else:
				s = z[i/100] + ' hundred and ' + z[r]
	l = reduce(lambda a, b: a + len(b), s.replace('-', '').split(), 0)
	total += l
	print(str(i) + '\t' + s + '\t' + str(l))

print(total)
