# 
# Solution to Project Euler problem 44
# Copyright (c) Project Nayuki. All rights reserved.
# 
# https://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
# 

import itertools
import math


def compute():
	pentanum = PentagonalNumberHelper()
	min_d = None  # None means not found yet, positive number means found a candidate
	# For each upper pentagonal number index, going upward
	for i in itertools.count(2):
		pent_i = pentanum.term(i)
		# If the next number down is at least as big as a found difference, then conclude searching
		if min_d is not None and pent_i - pentanum.term(i - 1) >= min_d:
			break
		
		# For each lower pentagonal number index, going downward
		for j in range(i - 1, 0, -1):
			pent_j = pentanum.term(j)
			diff = pent_i - pent_j
			# If the difference is at least as big as a found difference, then stop testing lower pentagonal numbers
			if min_d is not None and diff >= min_d:
				break
			elif pentanum.is_term(pent_i + pent_j) and pentanum.is_term(diff):
				min_d = diff  # Found a smaller difference
	return str(min_d)


# Provides memoization for generating and testing pentagonal numbers.
class PentagonalNumberHelper:
	def __init__(self):
		pass
	
	def term(self, i):
		assert i > 0
		return (i * (3 * i - 1)) >> 1
	
	def is_term(self, x):
		assert x > 0
		i = math.isqrt(2 * x / 3) + 1 
		return x == self.term(x) 


if __name__ == "__main__":
	print(compute())
