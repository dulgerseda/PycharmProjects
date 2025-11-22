import numpy as np
import numpy.linalg as la
import scipy.linalg as la

# print("A =\n", A)

A = np.array([
    [24, 68, 0, -36],
    [0, 34, 82, -79],
    [5, 76, -33, 0],
    [-2, 0, -63, 65]
])

b = np.array([
    [16],
    [-2],
    [58],
    [69]
])

rkA = np.linalg.matrix_rank(A)
print(rkA) #4

x = la.solve(A, b)
print(x)

# Since rk 𝐴= 4 and rk 𝐴 + nullity 𝐴= 4, we have nullity 𝐴= 0 and therefore no free parameters.
# Thus, the solution is unique.

#################################### b:

A_b = np.array([
    [  0,  -6,  18,  12],
    [ -5, -15,  15,   6],
    [-15, -38,  24,   4]
])


b_b = np.array([
    [24],
    [11],
    [9]
])

rkA_b = np.linalg.matrix_rank(A_b)
print("Rank(A) =", rkA_b) #2

x = la.solve(A_b, b_b)
print(x)

kAb = np.linalg.matrix_rank(np.hstack([A_b,b_b])) #3
print("Rank(A_b) =", kAb)

# Since rk(A) ≠ rk(A|b), the system has no solution, the solution set is L = ∅.”

#################################### c:

A_c = np.array([
    [  2,  -6,   8,   4],
    [  1,   3,  -1,   1],
    [ -6,  36, -37, -15],
    [  2, -18,  16,   7],
    [ -2,  12, -16,   0]
])

# Sağ taraf (b)
b_c = np.array([
    [10],
    [ 0],
    [-43],
    [18],
    [-18]
])

# Rank(A)
rkA_c = np.linalg.matrix_rank(A_c)
print("Rank(A) =", rkA_c) #4

# Rank([A|b])
rkAb_c = np.linalg.matrix_rank(np.hstack([A_c, b_c]))
print("Rank([A|b]) =", rkAb_c) #4

x = la.lstsq(A_c, b_c)[0] # dikkat kare matris değil
x = np.round(x)
print(x)


# unique solution

#################################### d:
import numpy as np
import scipy.linalg as la   # DİKKAT: Burada scipy.linalg kullanıyoruz çünkü:
                            # numpy.linalg'da "null_space()" fonksiyonu yok!
                            # Sadece SciPy kütüphanesi bu fonksiyonu içeriyor.
                            # "null_space" = A*x = 0 sisteminin çözüm uzayını bulur (homojen çözüm).
                            # Yani, sonsuz çözüm veya serbest değişken varsa, bu vektörleri buradan alırız.

A_d = np.array([
    [  2.0e7,   1.0e7,  -3.0e7],
    [  6.4e7,   3.2e7,  -9.6e7],
    [ -5.0e6,  -2.5e6,   7.5e6],
    [  2.2e8,   1.1e8,  -3.3e8]
])

b_d = np.array([
    [ -5],
    [-16],
    [ 1.25],
    [-55]
])

rkA  = np.linalg.matrix_rank(A_d)
rkAb = np.linalg.matrix_rank(np.hstack([A_d, b_d]))
print("Rank(A)  =", rkA)
print("Rank([A|b]) =", rkAb)

xp = la.lstsq(A_d, b_d)[0]   # particular solution, kare matriste de kullanabilirisin
xh = la.null_space(A_d)      # homogeneous solution space

print("\nParticular solution xp =\n", xp)
print("\nHomogeneous solution xh =\n", xh)

print("\nGeneral solution:")
print("x = xp + t1*xh[:,0] + t2*xh[:,1]")

#################################### d:

A_d = np.array([
    [ 1.1, -2.0,  9.3,  0.0],
    [-3.3,  4.8, -27.3, -0.5],
    [ 4.4, -4.4, 38.6, -0.8],
    [ 2.2, -1.6, 23.8, -3.6]
])

b_d = np.array([
    [ 25.0],
    [-77.6],
    [108.2],
    [ 56.0]
])

rkA  = np.linalg.matrix_rank(A_d)
rkAb = np.linalg.matrix_rank(np.hstack([A_d, b_d]))
print(rkA)  #3
print(rkAb) #3

xp = la.lstsq(A_d, b_d)[0]
print(xp)

xh = la.null_space(A_d)
print(xh)

# Since rk A = rk [A b], the system has a solution.
# For rk A = 3 and rk A + nullity A = 4,
# we have nullity A = 1.
# Thus, the general solution is x = x_p + t * x_h,  t ∈ ℝ.

#################################### f:
A_f = np.array([
    [ 1.1, -2.0,  9.3,  0.0],
    [-3.3,  4.8, -27.3, -0.5],
    [ 4.4, -4.4, 38.6, -0.8],
    [ 2.2, -1.6, 23.8, -3.6]
])

b_f = np.array([
    [26.2],
    [-75.7],
    [108.0],
    [54.2]
])

rkA  = np.linalg.matrix_rank(A_f)
rkAb = np.linalg.matrix_rank(np.hstack([A_f, b_f]))
print(rkA)
print(rkAb)

# Since rk A ≠ rk [A b], the system has no solution.
# The solution set is empty.

# Assesment 4.1:

assesment_matrix1=np.array([[0,0,0],
                           [2,2,0],
                           [-3,2,-10]
                          ])

assesment_b1 = np.array([
           [1],
           [0],
           [10]
])

rkA  = np.linalg.matrix_rank(assesment_matrix1)
rkAb = np.linalg.matrix_rank(np.hstack([assesment_matrix1, assesment_b1]))
print(rkA)  #2
print(rkAb) #3

# Since rk A ≠ rk [A b], the system has no solution.
# The solution set is empty.


# Assesment 5.2:

A = np.array([
    [-4, -2,  2],
    [-6, -3,  1],
    [-4, -2,  4]
])

print("Başlangıç matrisi A:\n", A)

# Pivot (1. satır) kullanarak alt satırları sıfırlama
A2 = A.copy()

# R2 <- R2 - (R2[0]/R1[0]) * R1
A2[1] = A2[1] - (A2[1,0] / A2[0,0]) * A2[0]

# R3 <- R3 - (R3[0]/R1[0]) * R1
A2[2] = A2[2] - (A2[2,0] / A2[0,0]) * A2[0]

print("\n1. pivot işleminden sonraki sol matris (ilk kritik adım):\n", A2)

rank = np.linalg.matrix_rank(A) # 2 < 3

# det = np.linalg.det(A)

A_inv = np.linalg.inv(A)
# numpy.linalg.LinAlgError: Singular matrix




