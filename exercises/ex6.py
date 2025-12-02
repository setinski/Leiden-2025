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
	pass

# Plot the root hermite factor of SIS(n, 2*n, ceil(2**(3 + n/4)))
# for all n from 10 to 50. (Also print them as they are computed
# so that you can check intermediate results while the whole
# plot is being computed which may take a few minutes)



# Define C to be experimental limit of the root hermite factor
# (The following should maatch your experiment roughly)

C = 1.035 

# Using C, n, m, q, predict the length of a solution to SIS using LLL:

def predict_SIS_solution_length(n, m, q):



	