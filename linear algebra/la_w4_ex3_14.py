
import numpy as np


# A matrisi (4x3)
A = np.array([[3, 1, 1],
              [1, 3, 1],
              [2, 1, 1],
              [2, 0, 4]])

# B matrisi (3x3)
B = np.array([[2, 1, 2],
              [2, 1, 0],
              [0, 1, 1]])

# Matris çarpımı
C = A @ B.T

print("A =\n", A)
print("B =\n", B)
print("C = A × B =\n", C)


A.shape #(4,3)
A.size

B.shape # (3,3)

C.shape  # (4.3)

# I.e., 𝑎𝑖 𝑗 is the number of units of flour 𝐹𝑖 needed to
# produce one unit of dough 𝐷 𝑗 , and 𝑏𝑘 𝑗 is the number of units of dough 𝐷 𝑗 needed to
# produce one bread of type 𝐵𝑘.

# [[9  7  2]
#  [7  5  4]
#  [7  5   2]
#  [12  4  4]]

# Columns of A = rows of B,  hamur x ekmek

# bread quantities: 10xB1, 5xB2, 15xB3
x = np.array([[10], [5], [15]])

# flour needed = C * x
flour_needed = C @ x

print("\nFlour needed (F1-F4):\n", flour_needed)
# Flour needed (F1-F4):
# [[155]
# [155]
# [125]
# [200]]


######## ASSESMENTS:

A = np.array([[1, 0, -4],
              [-2, 1, 4],
              [0, 2, -1]])

B = np.array([[4, 3],
              [-3, 1],
              [1, 0]])

C = np.array([[2, 3, 1]])

A2 = A @ A

AB = A @ B

# AB^T (Tanımsız, çünkü boyutlar uyuşmaz)
# 2A + 3C (Tanımsız)

ACt = A @ C.T

# B^2 (Tanımsız)

CA = C @ A

CtC = C.T @ C

