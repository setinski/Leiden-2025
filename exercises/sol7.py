import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, log, exp, ceil
from sys import exit
from sol5 import LLL, gram_schmidt_decomposition
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


import matplotlib.pyplot as plt

rep = 5
R = []
P = []
M = list(range(30, 100, 2))
for m in M:
  real = 0
  for r in range(rep):
      real += log(measure_SIS_solution_length(20, m, 67))/rep
  pred = log(predict_SIS_solution_length(20, m, 67))
  R.append(real)
  P.append(pred)
  print(m, pred, real)
    

plt.plot(M, R)
plt.plot(M, P)
plt.ylabel('log ||b_1||')
plt.xlabel('m')
plt.show()




# Try to understand what is going on by looking at the profile
# of a basis for relevant values of m.


for m in [30, 60, 100]:
    B = random_SIS_lattice(20, m, 67)
    list(LLL(B))
    L, D, Q = gram_schmidt_decomposition(B)
    print(m)
    plt.plot(range(m), np.log(np.abs(D)), label="m = %d"%m)

plt.ylabel('log ||b_i||')
plt.xlabel('i')
plt.legend(loc="upper right")
plt.show()
