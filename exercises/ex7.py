import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, log, exp, ceil
from sys import exit
from sol5 import LLL
from sol6 import *

# Measure the length of the first vector found by LLL on a
# SIS lattice with parameters n, m, q

def measure_SIS_solution_length(n, m, q):
	B = random_SIS_lattice(n, m, q)
	list(LLL(B))
	return sqrt(B[0] @ B[0])

# Compare with a plot the prediction those measurement to the
# prediction made in ex6 for n = 20, q = 67 and m growing from 30 to 120.
# using a logarithmic scale

if __name__ == "__main__":
	import matplotlib.pyplot as plt
	L, J = [], []
	n = 20
	q = 67
	for m in range(30, 100):
		J.append(log(measure_SIS_solution_length(n, m, q)))
		L.append(log(predict_SIS_solution_length(n, m, q)))
		print(m, J[-1], L[-1])

	plt.plot(range(30, 100), L)
	plt.plot(range(30, 100), J)
	plt.show()

# Try to understand what is going on by looking at the profile
# of a basis for relevant values of m.

# look at values m = 30, m = 60 and finally m = 100 

