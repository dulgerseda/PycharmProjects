
import numpy as np
import scipy.linalg as la

# print("A =\n", A)

#---------------------- 6.1.c
A = np.array([[1, -2, 1, 1],
              [3,  2, -2, 2],
              [-1, 2,  0, -1],
              [1,  2,  5, 1]])

np.linalg.det(A)

#---------------------- 6.2.b

A = np.array([[-2, 1, 0, 0],
              [1, -2, 1, 0],
              [0, 1, -2, 1],
              [0, 0, 1, -2]])

d=np.linalg.det(A)
print(f"{d:.2f}")

#----------------------

A = np.array([
    [1, 2, 0, -1],
    [-3, -3, 6, -3],
    [2, -1, -5, -7],
    [-3, -10, -4, 3]])
d = np.linalg.det(A)
print(f"{d:.2f}")
