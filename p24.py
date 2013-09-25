# 1000000th Lexicographic Permutation #
from math import factorial

final_answer = []
final_answer_str = ""
available_digits = range(0,10)
desired_rank = pow(10,6) + 1

current_rank = 1


while len(final_answer) != 10:
	index = 0
	n = len(available_digits)
	print available_digits
	while True:
		rank_increase = factorial(n-1)
		if current_rank + rank_increase < desired_rank:
			current_rank += rank_increase
			print "%dth permutation" % current_rank
			index += 1
		else:
			print "added digit: %d" % available_digits[index]
			final_answer.append(available_digits[index])
			final_answer_str += str(available_digits[index])
			print "partial answer: " + str(final_answer)
			available_digits.pop(index)
			break
	
	
		
print final_answer_str

