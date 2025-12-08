import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, log, exp, ceil
from sys import exit
from sol5 import LLL
from sol6 import random_SIS_lattice


# Measure the length of the first vector found by LLL on a 
# SIS lattice with paramenters n, m, q

def measure_SIS_solution_length(n, m, q):
	B = random_SIS_lattice(n, m, q)
	list(LLL(B))
	return sqrt(B[0] @ B[0])

# Compare with a plot the prediction those measurement to the
# prediction made in ex6 for n = 20, q=67 and m growing from 30 to 120.
# using a logarithmic scale

def plot_SIS():
    result=[]
    rep=5
    for i in range(30,100,5): #steps of 5
        x = 0
        for r in range(rep):
            x += measure_SIS_solution_length(20, i, 67)
        print(i, x/rep)
        result.append(x/rep)

    plt.scatter(range(30,100,5), result)
    plt.xlim(30, 100)
    plt.xlabel("m")
    plt.ylabel("prediction")
    plt.title("SIS")

    plt.show()
    return

#Try to understand what is going on by looking at the profile
# of a basis for relevant values of m.


############
# Main runner
############ 
if __name__ == "__main__":
    plot_SIS()