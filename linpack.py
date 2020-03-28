import numpy as np
import scipy.linalg
from time import time

N = 1000

np.random.seed(3)

A = np.random.rand(N,N) - 0.5

X = np.ones(N)

B = np.random.rand(N)

t1 = time()
P, L, U = scipy.linalg.lu(A)
t2 = time()

tiempo1 = t2 - t1

t1 = time()
Ai = scipy.linalg.inv(A)
np.dot(Ai,B)
t2 = time()

tiempo2 = t2 - t1

print("Tiempo de factorización:", tiempo1, "s")
print("Tiempo de solución:", tiempo2, "s")
