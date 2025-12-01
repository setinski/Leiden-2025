import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, log, exp
from sys import exit
from sol5 import LLL

# This function returns the basis of an SIS lattice
def random_SIS_lattice(n, m, q):
	B = np.block([[q * np.identity(m-n), np.zeros((m-n, n))],
				  [np.random.randint(q, size=(n, m-n)), np.identity(n)]])
	return B


# Measure the root hermite factor of LLL on a SIS lattice: 
# the value c such that ||b_1|| = c^(m-1) * det(L)^{1/n}
# Note: the determinant can be predicted from n, m, q
def measure_rhf(n, m, q):
	pass

# Plot the root hermite factor of SIS(n, 2*n, 2**(3 + n/4))
# for all n multiple of 5.
