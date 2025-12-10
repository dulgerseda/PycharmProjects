from week_7.exercise_kwargs_solution import my_dict

# ===============================================================
# WEEK SUMMARY — Python: Copying, Lambda, Comprehension, Typing
# ===============================================================
# Bu dosya şu konuları kapsar:
# 1. Assignment (atama) farkı
# 2. copy() – shallow vs deep copy
# 3. clone örneği
# 4. Lambda fonksiyonları
# 5. Lambda ile map(), sort(), filter()
# 6. List Comprehension (temel, koşullu, iç içe)
# 7. Dictionary Comprehension
# 8. Type Annotations (ve assert kontrolü)
# ===============================================================

# ---------------------------------------------------------------
# 1️⃣ Assignment (Atama)
# ---------------------------------------------------------------
print("=== Assignment örneği ===")
a = [1, 2, 3]
b = a  # sadece referans kopyalanır, yeni liste oluşmaz
b.append(4)
print("a:", a)  # [1, 2, 3, 4]  → çünkü aynı referans
print("b:", b)

# ---------------------------------------------------------------
# 2️⃣ copy() — Shallow Copy
# ---------------------------------------------------------------
print("\n=== Shallow Copy ===")
import copy

a = [[1, 2], [3, 4]]
b = a.copy()  # shallow copy: dış liste kopyalanır ama içtekiler referans kalır
b[0].append(99)

print("a:", a)  # [[1, 2, 99], [3, 4]]
print("b:", b)  # [[1, 2, 99], [3, 4]]
print("id(a[0]) == id(b[0]) →", id(a[0]) == id(b[0]))  # True (aynı iç liste)

# ---------------------------------------------------------------
# 3️⃣ Deep Copy
# ---------------------------------------------------------------
print("\n=== Deep Copy ===")
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)  # tamamen yeni bir kopya oluşturur
b[0].append(99)

print("a:", a)  # [[1, 2], [3, 4]]  → etkilenmez
print("b:", b)  # [[1, 2, 99], [3, 4]]
print("id(a[0]) == id(b[0]) →", id(a[0]) == id(b[0]))  # False

# ---------------------------------------------------------------
# 4️⃣ Clone (aynı nesneden bağımsız kopya)
# ---------------------------------------------------------------
print("\n=== Clone örneği ===")
original = [1, 2, 3]
clone = original[:]  # slicing ile shallow copy
clone.append(4)

print("original:", original)  # [1, 2, 3]
print("clone:", clone)        # [1, 2, 3, 4]
print("id(original) == id(clone) →", id(original) == id(clone))  # False


# ---------------------------------------------------------------
# 5️⃣ Lambda Function
# ---------------------------------------------------------------
print("\n=== Lambda Fonksiyonları ===")

# Normal fonksiyon
def square(x):
    return x * x

# Lambda (anonim fonksiyon)
square_lambda = lambda x: x * x

print(square(5), square_lambda(5))  # 25, 25

# ---------------------------------------------------------------
# 6️⃣ Lambda ile map(), sort(), filter()
# ---------------------------------------------------------------
print("\n=== map(), sort(), filter() örnekleri ===")
import math

# map() — listedeki her elemana işlem uygular
angles = [0, 15, 30, 45, 60, 75, 90]
cos_values = list(map(lambda z: round(math.cos(math.radians(z)), 3), angles))
print("cos_values:", cos_values)

# sort() — sıralama anahtarını belirle
nums = [6, 1, 3, 7, 9, 5, 2, 4, 8, 0]
nums.sort(key=lambda x: x % 3)
print("sorted nums:", nums)

# filter() — koşulu sağlayanları döndür
evens = list(filter(lambda x: x % 2 == 0, range(10)))
print("even numbers:", evens)


# ---------------------------------------------------------------
# 7️⃣ List Comprehension
# ---------------------------------------------------------------
print("\n=== List Comprehension ===")

# Basit örnek
x = [1, 2, 3, 4, 5]
squares = [i ** 2 for i in x]
print("Kareler:", squares)

# Koşullu (if ile)
even_squares = [i ** 2 for i in x if i % 2 == 0]
print("Çift sayıların kareleri:", even_squares)

# If–Else kısa yazımı
conditional = [i ** 2 if i % 2 == 0 else -i for i in x]
print("If–Else sonucu:", conditional)

nested_list = [[1000, 200, 30], [22, 33], [555, 333, 222, 111]]
res = []
for sub in nested_list:        # dış listeyi dön
    for y in sub:              # iç listedeki her elemanı dön
        res.append(y // 10)

# İç içe (nested)
nested_list = [[1000, 200, 30], [22, 33], [555, 333, 222, 111]]
flattened = [y // 10 for sub in nested_list for y in sub]
print("Flattened (//10):", flattened)

# Nested yapıyı korumak için:
nested_result = [[y // 10 for y in sub] for sub in nested_list]
print("Nested sonucu:", nested_result)

# ---------------------------------------------------------------
# 8️⃣ Dictionary Comprehension
# ---------------------------------------------------------------
print("\n=== Dictionary Comprehension ===")

a = [1, 2, 3, 6, 10]
d1 = {elem: elem for elem in a}  # basit key:value
print("d1:", d1)

d2 = {pos: elem for pos, elem in enumerate(a)}  # enumerate ile
print("d2:", d2)

keys = ['a', 'b', 'c', 'd', 'e']
d3 = {k: v for k, v in zip(keys, a)}  # zip ile
print("d3:", d3)


# ---------------------------------------------------------------
# 9️⃣ Type Annotations (Tip ipuçları)
# ---------------------------------------------------------------
print("\n=== Type Annotations ===")
from typing import List

# Tip belirterek fonksiyon tanımı
def myfunc(a: List[str]) -> str:
    print(a)
    return a[0]

result = myfunc(['a', 'b'])
print("Sonuç:", result)

# Assert ile runtime tipi kontrol etme
def myfunc_strict(a: List[str]) -> str:
    assert type(a) == list, "myfunc needs a list of strings as parameter a."
    print(a)
    return a[0]

myfunc_strict(['x', 'y'])   # doğru
# myfunc_strict(3)          # AssertionError: myfunc needs a list of strings as parameter a.


### SW12 - LAMBDA

my_list = [10, 50, 25, 70, 5]

my_list = [x**2 if x < 30 else x for x in my_list]
my_list.sort()

nums.sort(key=lambda i: i ** 2 if i < 30 else i)

my_list = [338, 693, -19, 144, 85, 958, 495, -218, 647, 50, 337, 869,
           537, 477, -625, 31, 173, 795, -61, 257, 983, 415, 16, 112, -53]
# Use the function sort and pass a lambda function to the keyword parameter
# 'key' to sort my_list in two different ways:

my_list.sort(key=lambda i: i ** 2 if i < 30 else i)
print("my_list:", my_list)

# sort only values less than 100 and keep all others in
# original order after the sorted values.

my_list.sort(key=lambda x: (0, x) if x < 100 else (1, my_list.index(x)))
print(my_list)

#-------

# 1. 100'den küçükleri sırala
small = sorted([x for x in my_list if x < 100])

# 2. 100 ve üstünü aynen koru
others = [x for x in my_list if x >= 100]

result = small + others
print(result)

# 🔹 Orijinal liste
my_list = [338, 693, -19, 144, 85, 958, 495, -218, 647, 50,
           337, 869, 537, 477, -625, 31, 173, 795, -61, 257,
           983, 415, 16, 112, -53]

# 🔹 enumerate() her elemana bir sıra numarası (index) ekler
# [(0, 338), (1, 693), (2, -19), (3, 144), ...]
indexed = list(enumerate(my_list))

# 🔹 Şimdi her eleman t = (index, value) şeklinde bir tuple (çift)
#   t[0] = index (sıradaki konumu)
#   t[1] = value (sayının kendisi)
# 🔹 Lambda fonksiyonu sıralama anahtarını (key) belirler:
#   - Eğer sayı (t[1]) < 100 → key = (0, t[1])   → önce gelir, değere göre sıralanır
#   - Eğer sayı (t[1]) >= 100 → key = (1, t[0])   → sonra gelir, orijinal sırayı korur
indexed.sort(key=lambda t: (0, t[1]) if t[1] < 100 else (1, t[0]))

# 🔹 Sıralı listedeki sadece sayıları geri çıkar
result = [t[1] for t in indexed]

print(result)

### SW13 - LIST COMPREHENSION

from random import random

my_num = []

for i in range(330):
    my_num += [int(random() * 1000)]

my_vars = [my_num[i*15:(i+1)*15] for i in range(22)]

print(*my_vars, sep='\n')

### SW13 - FUZZ_SUM

def fuzz_sum(data, offset=0):
    hat_coeff = [1, 2, 3, 2, 1]
    x = data['x']
    w = len(hat_coeff)
    half_w = w // 2
    results = [None] * len(x)

    for i in range(half_w, len(x) - half_w):
        window = x[i - half_w: i + half_w + 1]
        total = sum(a * b for a, b in zip(window, hat_coeff))
        position = i + offset
        if position < len(x):
            results[position] = total

    return results


# 🔹 Test:
data = {'name': 'test', 'loc': 'north',
        'x': [72, 42, 88, 23, 17, 35, 1, 69, 81, 25, 56, 28, 41,
              16, 33, 72, 49, 28, 29, 64, 53, 75, 39, 24, 4, 21, 25]}

print(fuzz_sum(data))

"""

i = 2
window = data[i - half_w : i + half_w + 1]
       = data[0 : 5]
       = [72, 42, 88, 23, 17]

(72×1) + (42×2) + (88×3) + (23×2) + (17×1)
= 72 + 84 + 264 + 46 + 17 = 483

pos = i + offset = 2 + 3 = 5
Yani bu 483 sonucu, results[5] konumuna yazılır.
[None, None, None, None, None, 483, None, None, ...]

"""