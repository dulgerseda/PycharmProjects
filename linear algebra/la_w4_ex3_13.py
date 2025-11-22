import numpy as np

# -----------------------------------------------------------
# a) In Python, define in a most simple way the following matrices.
# M = [[1, 7],
#      [4, 2]]
#
# N = [[6, 0],
#      [0, 5]]
#
# P = [[-π, -π],
#      [-π, -π]]
#
# Q = [[e + √2, e],
#      [e, e + √2]]
#
# Hint:
# Use np.e for Euler’s number and np.pi for π.
# Use np.sqrt(2) for √2.
# -----------------------------------------------------------

M = np.array([[1, 7],
              [4, 2]])

N = np.array([[6, 0],
              [0, 5]])

P = -np.pi * np.ones((2, 2))  # all entries = -π

Q = np.array([[np.e + np.sqrt(2), np.e],
              [np.e, np.e + np.sqrt(2)]])

print("M =\n", M)
print("N =\n", N)
print("P =\n", P)
print("Q =\n", Q)


# -----------------------------------------------------------
# b) Define the block matrix R =
#     [ M  N ]
#     [ P  Q ]
#
# Use np.block() to create this structure.
# -----------------------------------------------------------

R = np.block([[M, N],
              [P, Q]])

print("\nR =\n", R)


# -----------------------------------------------------------
# c) Define the block matrix S =
#     [ M + N     O₂,₂ ]
#     [  O₂,₂   (1/π)P ]
#
# where O₂,₂ is the 2×2 zero matrix.
# -----------------------------------------------------------

O22 = np.zeros((2, 2))  # 2×2 zero matrix

S = np.block([[M + N, O22],
              [O22, (1/np.pi) * P]])

print("\nS =\n", S)


# b) Find the format (shape) of R with a suitable command.

R = np.block([[M, N],
              [P, Q]])

print(R.shape)



# c) Calculate the following:

R_plus_S = R + S
R_transpose = R.T
MN = M @ N
NM = N @ M

print("R + S =\n", R_plus_S, "\n")
print("Rᵀ =\n", R_transpose, "\n")
print("M·N =\n", MN, "\n")
print("N·M =\n", NM, "\n")


# Element-wise operations are possible only when the dimensions are equal,
# or when broadcasting rules apply.
# Element-wise product (Hadamard product)
elementwise_product = M * N

# Element-wise power
elementwise_power = M ** N

print("Element-wise product (M * N) =\n", elementwise_product)
print("\nElement-wise power (M ** N) =\n", elementwise_power)

# e)
# Read out the second to fourth columns of S as well as the first and third column of R (in this order).
# Read out the second and last column of R in reversed order.

S = np.block([[M + N, O22],
              [O22, (1/np.pi) * P]])

print("\nS =\n", S)


S[:, 1:4]       # S matrisinin 2.–4. sütunları



R = np.block([[M, N],
              [P, Q]])

print("\nS =\n", R)

R[:, [0, 2]]    # R matrisinin 1. ve 3. sütunları
R[:, [3, 1]]    # R matrisinin son ve ikinci sütunu (ters sıra)

# f)
# Interchange the second and fourth column of R.
# Multiply the first column of R by 2.
# Now exchange the third row of R by the sum of the first and the second.

R[:, [1, 3]] = R[:, [3, 1]]

R1x2  = 2 * R[:, 0]              # 1. sütunu 2 ile çarp

R[2, :] = R[0, :] + R[1, :]        # 3. satırı = 1. + 2. satır

