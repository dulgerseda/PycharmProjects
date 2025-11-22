
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


#----------------------ex-1
A = np.array([[2,-3],[3,5]])
b = np.array([1, 2])
x = np.linalg.solve(A, b)
print(x)

#---another solution
A = np.array([[2,-3],[3,5]])
b = np.array([1, 2])
x1 = np.linalg.inv(A)@b
print(x1)

#---another solution-scipy
A = np.array([[2,-3],[3,5]])
Ainv = np.linalg.inv(A)
b = np.array([1, 2])
x2 = Ainv@b
print(x2)

print(A@x1-b)
print(A@x2-b)

#Usually: Linear algebra methods of scipy should be used



#----------------------ex-2
A = np.array([[-2,3,1],[3,-2,0], [1,0,3]])
b = np.array([[-7], [-3], [-2]])
x = np.linalg.solve(A, b)
print(x)

#----------------------ex-3
A = np.array([[-2,3,1],[4,-6,-2], [1,0,3]])
b = np.array([[-7], [-3], [-2]])
x = np.linalg.solve(A, b)
print(x)

# numpy.linalg.LinAlgError: Singular matrix, the first two columns are linear dependent

d = np.linalg.det(A) #check the det to show that the matris is singular or not
print(d)
print(f"{d:.2f}")

# also det = 0

#----------------------scipy/numpy

A = np.random .random (9)
A. shape = [3 ,3]
b = np.random .random (3)
b. shape = [3 ,1]
x1 = la.inv(A)@b
x2 = la.solve(A, b)
print("Error with inv: ", la.norm(A@x1 -b))
print("Error with solve: ", la.norm(A@x2 -b))

# For solving a systems of linear equations: Preferred method is
# scipy.linalg.solve() compared to inverting coeﬃcient matrix

"""scipy.linalg.solve() is preferred over la.inv(A) @ b for solving linear systems 
because it is faster, more numerically stable, and uses less memory.
Error with inv:  1.6653345369377348e-16
Error with solve:  1.1102230246251565e-16
"""

#----------------------
A = np.array([[1,1],[1,0.999]])
b = np.array([[1],[1]])
x = la.solve(A, b)
print(x)

A = np.array([[1.001,1.001],[1,0.999]])
b = np.array([[1],[1]])
x = la.solve(A, b)
print(x)

#----------------------
A = np.array([[2,-6],[-1,3]])
b = np.array([[-2],[1]])
x = la.solve(A, b)
print(x)

d = np.linalg.det(A) #0
print(d)

x=la.lstsq(A,b)[0]
print(x)
print(A@x-b)

#----------------------
A = np.array([[2,-6],[-1,3]])
b = np.array([[1],[1]])
x = la.solve(A, b)
print(x)

d = np.linalg.det(A) #0
print(d)

x=la.lstsq(A,b)[0]
print(x)
print(A@x-b)

"""Python may return “solutions” of linear systems which are no solutions!"""

#----------------------
A = np.array([[2,-6],[-1,3]])
b = np.array([[-2],[1]])
x = la.solve(A, b)
print(x)

x_h = la.null_space(A) #direction vector
print(x_h)

"""Solve an under-determined system just with scipy.linalg.lstsq()"""

#---------------------Example: In a mineral oil refinery: 4 equation, 5 unknown; undetermined system
A = np.array ([
[1 ,1 ,0 ,0 ,0],
[1,0,-1,-1,0],
[0,1,1,0,-1],
[0 ,0 ,0 ,1 ,1]
])
b = np.array ([[50] , [0] , [0] , [50]])
f = la.lstsq(A, b)[0]
print(f)

rkA = np.linalg.matrix_rank(A)
Ab = np.hstack([A,b])
rkAb = np.linalg.matrix_rank(Ab)
print(rkA)
print(rkAb)

"""Two ranks are equal: System is consistent
But see more
Dimension formula:
rk A + nullity A = 5 ⇒ 3 + nullity Ax = 5 General solution of system has two free parameters
Infinitely many solutions
General solution:
x_h = la.null_space(A)
print(x_h)"""

x_h = la.null_space(A)
print(x_h)

#-----------------------   EXERCISES 7  --------------------------#
#----------------------7.1:

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
rkAb = np.linalg.matrix_rank(np.hstack([A, b]))  # augmented matrix
print("rank(A) =", rkA)
print("rank(A|b) =", rkAb)

"""
rank(A) = 4
rank(A|b) = 4
Since rk 𝐴= 4 and rk 𝐴 + nullity 𝐴= 4, we have nullity 𝐴= 0 and therefore no free
parameters. Thus the solution is unique.
"""

x = la.solve(A, b)
print(x)

#----------------------

A = np.array([
[0, -6, 18, 12],
[-5, -15, 15, 6],
[-15, -38, 24, 4]
])
b = np.array([
[24],
[11],
[9]
])
rkA = np.linalg.matrix_rank(A)
rkAb = np.linalg.matrix_rank(np.hstack([A,b]))
print(rkA) #2
print(rkAb) #3 , no solution

#----------------------
A = np.array([
[2, -6, 8, 4],
[1, 3, -1, 1],
[-6, 36, -37, -15],
[2, -18, 16, 7],
[-2, 12, -16, 0]
])
b = np.array([
[10],
[0],
[-43],
[18],
[-18]
])

"""undetermined, çözüm varsa; la.lstsq(A,b)[0] kullan"""

rkA = np.linalg.matrix_rank(A)
rkAb = np.linalg.matrix_rank(np.hstack([A,b]))
print(rkA)
print(rkAb)

"""unique solution, -3.3e-15’ler sayısal sıfır"""

x = la.lstsq(A, b)[0]
print(x)

#----------------------
A = np.array([
[2e7, 1e7, -3e7],
[6.4e7, 3.2e7, -9.6e7],
[-5e6, -2.5e6, 7.5e6],
[2.2e8, 1.1e8, -3.3e8]
])
b = np.array([
[-5],
[-16],
[1.25],
[-55]
])

rkA = np.linalg.matrix_rank(A)
rkAb = np.linalg.matrix_rank(np.hstack([A,b]))
print(rkA)
print(rkAb)

xp = la.lstsq(A, b)[0]
print(xp)
xh = la.null_space(A)
print(xh)

#----------------------
A = np.array([
[1.1, -2, 9.3, 0],
[-3.3, 4.8, -27.3, -0.5],
[4.4, -4.4, 38.6, -0.8],
[2.2, -1.6, 23.8, -3.6]
])

b = np.array([
[25],
[-77.6],
[108.2],
[56]
])

rkA = np.linalg.matrix_rank(A)
rkAb = np.linalg.matrix_rank(np.hstack([A,b]))
print(rkA)
print(rkAb)
xp = la.lstsq(A, b)[0]
print(xp)
xh = la.null_space(A)
print(xh)

#----------------------
A = np.array([
[1.1, -2, 9.3, 0],
[-3.3, 4.8, -27.3, -0.5],
[4.4, -4.4, 38.6, -0.8],
[2.2, -1.6, 23.8, -3.6]
])

b = np.array([
[26.2],
[-75.7],
[108],
[54.2]
])

rkA = np.linalg.matrix_rank(A)
rkAb = np.linalg.matrix_rank(np.hstack([A,b]))
print(rkA) #3
print(rkAb) #4

# The system has no solution!


#----------------------7.2:
M = np.array([
    [1, 1, 2, 3, 0],
    [0, 1, 3, 3, 0],
    [1, 2, 2, 1, 1],
    [2, 4, 0, 1, 1],
    [0, 2, 3, 1, 1]
])

rho_mix = np.array([0.87, 1.00, 1.04, 0.86, 1.17]).T
Vsum = np.sum(M, axis=1)
b = rho_mix * Vsum

rkM = np.linalg.matrix_rank(M)
rkMb = np.linalg.matrix_rank(np.column_stack((M, b)))

print("rank(M)  =", rkM)
print("rank([M|b]) =", rkMb)


# Yeni karışımı ekle (sadece Liquid 5 içeren)
M_new = np.vstack([M, [0, 0, 0, 0, 1]])

# Yeni karışımın yoğunluğu (örnek değer verelim, diyelim ki ρ5 = 1.00)
b_new = np.append(b, 1.00)


rkM = np.linalg.matrix_rank(M_new)
print("rank(M_new) =", rkM) #5, unique

values= la.lstsq(M_new, b_new)[0]
print(values)
print(np.round(values, 2))


#----------------------7.3:
A = np.array([
[-1,0,0,0,0,0,0,1,0,0,0,0],
[1,1,0,0,0,0,0,0,-1,0,0,0],
[0,-1,1,0,0,0,0,0,0,0,0,0],
[0,0,-1,-1,0,0,0,0,0,1,0,0],
[0,0,0,1,-1,0,0,0,0,0,0,0],
[0,0,0,0,1,1,0,0,0,0,-1,0],
[0,0,0,0,0,-1,1,0,0,0,0,0],
[0,0,0,0,0,0,-1,-1,0,0,0,1],
[0,0,0,0,0,0,0,0,1,-1,1,-1]
])
b = np.array([[-9, 0, 8, 3, 6, 0, -5, -3, 0]]).T
rkA = np.linalg.matrix_rank(A)
rkAb = np.linalg.matrix_rank(np.hstack([A,b]))
print(rkA)
print(rkAb)


f = la.lstsq(A, b)[0]
print(f)
fh = la.null_space(A)
print(fh)

#----------------------7.4:

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

# a) Veri tanımı

x = np.array([400., 450., 516., 551., 594., 503., 621., 626., 690., 737., 780., 718.])
y = np.array([9892, 10195, 11071, 10947, 11209, 11191, 11805, 11767, 12142, 12454, 13071, 13282])

plt.figure(figsize=(8,5))
plt.scatter(x, y, color='royalblue', label="Veri noktaları")

# b) Interpolation (12 noktadan geçen 11. dereceden polinom)

n = 11
k = np.arange(n + 1).reshape(1, -1)   # üsler [0..11]
xv = x.reshape(-1, 1)                 # sütun vektör
V = xv ** k                           # Vandermonde matrisi (12x12)
p = la.solve(V, y)                    # katsayıları çöz

# Interpolasyon eğrisini çiz
xp = np.linspace(400, 785, 300).reshape(-1, 1)
Vp = xp ** k
yp = Vp @ p
plt.plot(xp, yp, 'r--', label='11. derece interpolasyon')

# c) Regression (en iyi yaklaşan doğru, n=1)

n = 1
k = np.arange(n + 1).reshape(1, -1)
V = xv ** k                           # 12x2 matris [1, x]
g = la.lstsq(V, y, rcond=None)[0]     # en küçük kareler çözümü

# Regresyon doğrusunu çiz
Vp = xp ** k
yp = Vp @ g
plt.plot(xp, yp, 'g-', label=f"Regresyon doğrusu (y={g[0]:.1f}+{g[1]:.2f}x)")
plt.xlabel("Deaths by falling out of bed (US)")
plt.ylabel("Lawyers in Puerto Rico")
plt.title("Deaths vs. Lawyers – Interpolation & Regression")
plt.legend()
plt.grid(True)
plt.show()

#-----------------------   Asessment 7  --------------------------#
#----------------------7.1:

import numpy as np
import scipy.linalg as la

A = np.array([
    [1.94, 2.02, 0, 0, 0, 0, 0],
    [0, 0, 2.02, 1.50, 0, 0, 0],
    [0, 0, 0, 0, 1.58, 1.50, 2.28]
])

b = np.array([9.86, 8.54, 11.42])

# particular solution
xp = np.linalg.lstsq(A, b, rcond=None)[0]

# homogeneous solution (null space)
xh = la.null_space(A)

print("xp =\n", xp)
print("\nNull space (xh) =\n", xh)


A = np.array([
    [1.94, 2.02, 0,    0,    0,    0,    0   ],
    [0,    0,    2.02, 1.50, 0,    0,    0   ],
    [0,    0,    0,    0,    1.58, 1.50, 2.28]
], dtype=float)

rank_A = np.linalg.matrix_rank(A)
print("rank(A) =", rank_A) #3

b = np.array([9.86, 8.54, 11.42])

xp = np.linalg.lstsq(A, b)[0]
print(xp)

xh = la.null_space(A)
print(xh)


#----------------------7.2:

# Veriler
x = np.array([28, 23, 32, 35, 29, 30, 27, 34, 32])
y = np.array([403, 60, 640, 560, 293, 626, 449, 614, 256])

# En küçük kareler (y = a + b*x)
b, a = np.polyfit(x, y, 1)  # 1 = doğrusal (degree=1)
print("b =", b)
print("a =", a)

x=34
y= a + b * x
print(y)
