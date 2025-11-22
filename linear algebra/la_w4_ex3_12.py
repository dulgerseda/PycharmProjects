import numpy as np
from skimage.transform import rescale
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# ---------- 1. GÖRSELİ OKU VE HAZIRLA ----------

img = mpimg.imread('/Users/sedadulger/PyCharmProjects/linear algebra/stinkbug4.JPG')

# Görseli küçült
img = rescale(img, 0.2)

# Kenarları kırp
img = np.delete(img, np.arange(20), axis=0)
img = np.delete(img, np.arange(80, 100), axis=0)
img = np.delete(img, np.arange(20), axis=1)
img = np.delete(img, np.arange(80, 100), axis=1)

# Renk eşikleme (siyah pikselleri bulmak için)
col = np.zeros(img.shape[0] * img.shape[1])
k = 0
for i in np.arange(img.shape[0]):
    for j in np.arange(img.shape[1]):
        col[k] = np.round(0.99 * img[i, j, :], 0)
        k += 1

# (x, y) koordinatlarını oluştur
image = np.array([
    np.repeat(np.arange(img.shape[0]), img.shape[1]),
    np.tile(np.arange(img.shape[1]), img.shape[0])
]).T

# Görüntüyü merkeze taşı
image[:, 0] -= 40
image[:, 1] -= 40

# Sadece siyah pikselleri seç
image = image[col == 0, :]

# ---------- 2. GÖRSELİN İLK HALİNİ ÇİZ ----------
plt.plot(image[:, 0], image[:, 1], "o", color="black")
plt.axis("square")
plt.xlim(-40, 40)
plt.ylim(-40, 40)
plt.title("Original image")
plt.show()

# ---------- 3. MATRİSLERİ TANIMLA ----------

A = np.array([[0, 1],
              [1, 0]])

B = np.array([[2, 0],
              [0, 1]])

C = np.array([[0, -1],
              [-1, 0]])

print("A:", A.shape)
print("B:", B.shape)
print("C:", C.shape)
print("image:", image.shape)  # (1074, 2)


# ---------- 4. ÇARPIM YORUMU ----------
# No, the matrices A, B, and C cannot be multiplied with the matrix 'image'
# in its current form, because the inner dimensions do not match.
# After transposing 'image' (image = image.T) the multiplication becomes possible,
# but only from the left side.

# ---------- 5. TRANSPOZ AL VE ÇARPIM YAP ----------

image = image.T  # (1074, 2) → (2, 1074)

# Şimdi matrislerle çarpım mümkün
image_A = A @ image
image_B = B @ image
image_C = C @ image


# ---------- 6. PLOT FONKSİYONU ----------

def plot_image(image_mat, title):
    plt.plot(image_mat[0, :], image_mat[1, :], "o", color="black")
    plt.axis("square")
    plt.xlim(-40, 40)
    plt.ylim(-40, 40)
    plt.title(title)
    plt.show(block=True)


# ---------- 7. HER BİR DÖNÜŞÜMÜ GÖSTER ----------

# For each of the matrices 𝑋 = 𝐴, 𝐵, 𝐶 define image_X as the product of X and image.
# Plot the resulting images using the above function.
# How has the image been transformed by these matrices?


plot_image(image, "Original image")
plot_image(image_A, "Transformed by A")
plot_image(image_B, "Transformed by B")
plot_image(image_C, "Transformed by C")

# A @ image  → swaps x and y coordinates  → reflection across the line y = x
# (x ve y koordinatlarını değiştirir → y = x doğrusu boyunca yansıma)

# B @ image  → stretches the image along the x-axis (x values doubled)
# (x ekseninde 2 kat genişletir → yatay yönde uzama)

# C @ image  → rotates and reflects the image (combination of 180° rotation and mirroring)
# (görüntüyü 180° döndürür ve yansıtır → ters çevirme etkisi)

# Transform the bug first with A and then with B. Then reverse the order of A and B.
# Is the result the same? Repeat with the matrices A and C.

# ---------- Transformations ----------
# A → then B
image_AB = B @ (A @ image)

# B → then A
image_BA = A @ (B @ image)

# A → then C
image_AC = C @ (A @ image)

# C → then A
image_CA = A @ (C @ image)

# ---------- Plot Results ----------
plot_image(image_AB, "Transformed by A then B")
plot_image(image_BA, "Transformed by B then A")
plot_image(image_AC, "Transformed by A then C")
plot_image(image_CA, "Transformed by C then A")

# ---------- Answer ----------
# No, the results are not the same.
# Matrix multiplication is not commutative (A @ B ≠ B @ A),
# so transforming with A then B gives a different result than B then A.
# The same applies to A and C — the order of transformations matters.
# (Hayır, sonuçlar aynı değildir. Matris çarpımı değişmeli değildir,
# bu yüzden dönüşümlerin sırası sonucu değiştirir.)


# Confirm your observations from Part d) by calculating the products A·B, B·A, A·C, and C·A by hand.

A = np.array([[0, 1],
              [1, 0]])

B = np.array([[2, 0],
              [0, 1]])

C = np.array([[0, -1],
              [-1, 0]])

# ---------- Calculate matrix products ----------
AB = A @ B
BA = B @ A
AC = A @ C
CA = C @ A

print("A·B =\n", AB)
print("B·A =\n", BA)
print("A·C =\n", AC)
print("C·A =\n", CA)

# ---------- Results ----------
# A·B = [[0 1]
#        [2 0]]
#
# B·A = [[0 2]
#        [1 0]]
#
# A·C = [[-1 0]
#        [ 0 -1]]
#
# C·A = [[-1 0]
#        [ 0 -1]]

# ---------- Answer ----------
# A·B ≠ B·A → matrix multiplication is not commutative.
# The order of transformations changes the result.
# (A·B, B·A'dan farklıdır — matris çarpımı değişmeli değildir.)
#
# However, A·C = C·A → these two matrices commute.
# (Ama A ve C'nin çarpımı aynıdır → bu iki matris değişmelidir, sıraları fark etmez.)


