import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, log, exp, ceil
from sys import exit
from sol5 import LLL

# This function returns the basis of an SIS lattice
def random_SIS_lattice(n, m, q):
	B = np.block([[q * np.identity(n), np.zeros((n, m-n))],
				  [np.random.randint(q, size=(m-n, n)), np.identity(m-n)]])
	return B

# Measure the root hermite factor of LLL on a SIS lattice: 
# the value c such that ||b_1|| = c^(m-1) * det(L)^{1/n}
# Note: the determinant can be predicted from n, m, q

def measure_rhf(n, m, q):
	B = random_SIS_lattice(n, m, q)
	list(LLL(B))
	x = log(B[0] @ B[0])/2
	y = n * log(q) / m
	c = exp((x-y)/(m-1))
	return c

# Plot the root hermite factor of SIS(n, 2*n, ceil(2**(3 + n/4)))
# for all n from 10 to 50.

if __name__ == "__main__":
	import matplotlib.pyplot as plt
	L = []
	max_n = 50
	rep = 5
	for n in range(10, max_n):
		x = 0
		for r in range(rep):
			x += measure_rhf(n, 2*n, ceil(2**(3 + n/4)))
		print(n, x/rep)
		L.append(x/rep)

	plt.plot([2*n for n in range(10, max_n)], L, 'o-r')
	plt.ylabel('Root Hermite Factor')
	plt.ylabel('Dimension')
	plt.show()

# Define C to be experimental limit of the root hermite factor

C = 1.025

# Using C, n, m, q, predict the length of a solution to SIS using LLL:

def predict_SIS_solution_length(n, m, q):
	return C**m * q**(n/m)


