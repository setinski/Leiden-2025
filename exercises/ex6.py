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
    B=random_SIS_lattice(n,m,q)
    LLL(B, epsilon=0.01, animate=False)
    c=(np.linalg.norm(B[0])/(q**(n/m)))**(1/(m-1))
    return c

# Plot the root hermite factor of SIS(n, 2*n, ceil(2**(3 + n/4)))
# for all n from 10 to 50. (Also print them as they are computed
# so that you can check intermediate results while the whole
# plot is being computed which may take a few minutes)
    
def rhf_SIS():
    result=[]
    for i in range(10,50):
        temp=measure_rhf(i, 2*i, ceil(2**(3 + i/4)))
        print(temp)
        result.append(temp)

    plt.scatter(range(10,50), result)
    plt.xlim(10, 50)
    plt.xlabel("n")
    plt.ylabel("Root Hermite Factor")
    plt.title("Root Hermite Factor for SIS")

    plt.show()
    return

# Define C to be experimental limit of the root hermite factor
# (The following should match your experiment roughly)

C = 1.035 

# Using C, n, m, q, predict the length of a solution to SIS using LLL:

def predict_SIS_solution_length(n, m, q):
    return C**(m-1)*q**(n/m) ## since RHF: ||b_1||= c^(m-1) *(q^n)^{1/n} 



############
# Main runner
############ 
if __name__ == "__main__":
    rhf_SIS()