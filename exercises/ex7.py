import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, log, exp, ceil
from sys import exit
from sol5 import *
from sol6 import *


# Measure the length of the first vector found by LLL on a 
# SIS lattice with paramenters n, m, q

def measure_SIS_solution_length(n, m, q):
	B = random_SIS_lattice(n, m, q)
	list(LLL(B))
	return sqrt(B[0] @ B[0])

# Compare with a plot the prediction those measurement to the
# prediction made in ex6 for n = 20, q=67 and m growing from 30 to 120.
# using a logarithmic scale

def plot_SIS_and_profiles():
    meas=[]
    pred=[]
    rep=5
    domain=range(30,110,5) #steps of 5
    for i in domain: 
        x = 0
        for r in range(rep):
            x += log(measure_SIS_solution_length(20, i, 67))
        print(i, x/rep)
        meas.append(x/rep)
        pred.append(log(predict_SIS_solution_length(20, i, 67)))
    plt.plot(domain, meas)
    plt.plot(domain, pred)
    plt.scatter(domain, meas)
    plt.scatter(domain, pred)
    plt.xlim(30, 100)
    plt.xlabel("m")

    plt.show()

    for i in [30, 60, 100]:
        B = random_SIS_lattice(20, i, 67)
        list(LLL(B))
        _, D, _ = gram_schmidt_decomposition(B)
        plt.plot(range(i), np.log(np.abs(D)))
    plt.show()
    return

#Try to understand what is going on by looking at the profile
# of a basis for relevant values of m=30,60,100.


############
# Main runner
############ 
if __name__ == "__main__":
    plot_SIS_and_profiles()