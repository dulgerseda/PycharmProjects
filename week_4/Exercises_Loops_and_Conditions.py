###################
# Exercise 1
###################
"""
Write a python program that constructs the following pattern using a nested for loop:

*
**
***
****
*****
****
***
**
*

HINT: print(yourstring, end="") -> the end parameter allows you to force python to stay on current line, compared to the default value of '\n'.
"""


n=5

for i in range(n):
    for j in range(i):
        print("* ", end="")
    print("")

for i in range(n,0,-1):
    for j in range(i):
        print("* ", end="")
    print("")

###########

n = 5
# Üst kısım (artan yıldız sayısı)
for i in range(1, n + 1):
    stars = "*" * (2 * i - 1)               # Her satırda yıldız sayısı: 1, 3, 5, 7, 9 ...
    print(stars.center(2 * n - 1))          # Satırı (2*n - 1) genişlikte ortala

# Alt kısım (azalan yıldız sayısı)
for i in range(n - 1, 0, -1):
    stars = "*" * (2 * i - 1)               # Her satırda yıldız sayısı: 7, 5, 3, 1 ...
    print(stars.center(2 * n - 1))          # Satırı (2*n - 1) genişlikte ortala

n = 5
for i in range(1, n + 1):
    stars = "*" * i
    print(stars.ljust(n))   # sola hizala

for i in range(n - 1, 0, -1):
    stars = "*" * i
    print(stars.ljust(n))

n = 5
for i in range(1, n + 1):
    stars = "*" * i
    print(stars.rjust(n))   # sağa hizala

for i in range(n - 1, 0, -1):
    stars = "*" * i
    print(stars.rjust(n))


###################
# Exercise 2
###################
"""
Write a python program to count the number of even and odd numbers contained in a sequence of numbers.
Example:
numbers = (1,2,3,4,5,6,7,8,9,10)
Output:
Number of even numbers: 5
Number of odd numbers: 5
"""

numbers = (1,2,3,4,5,6,7,8,9,10)

odd_numbers = []
even_numbers = []

for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print(len(even_numbers))
print(len(odd_numbers))


###################
# Exercise 3
###################
"""
Write a Python program which takes two digits m (row) and n (column) as input and
generates a two-dimensional structure (e.g. nested list). The value in the i-th row and j-th column 
should be i*j.
Note :
i = 0, 1, … , m-1
j = 0, 1, … , n-1
Input Test Data - Rows = 3
Input Test Data - Columns = 4
Expected Result: [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
"""

rows = int(input("row number: "))
cols = int(input("column number: "))

result_list = []

for i in range(rows):
    inner_list = []
    for j in range(cols):
        value = i*j
        inner_list.append(value)
    result_list.append(inner_list)
print(result_list)

# row number: >? 5
# column number: >? 5
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]]


###################
# Exercise 4
###################
"""
Write a Python program to find all numbers between 200 and 500 (limits included) only containing even digits.
Correct solution: 
200,202,204,206,208,220,222,224,226,228,240,242,244,246,248,260,262,264,266,26
8,280,282,284,286,288,400,402,404,406,408,420,422,424,426,428,440,442,444,446,
448,460,462,464,466,468,480,482,484,486,488
"""

result = []

for i in range(200, 501):
    s = str(i)
    all_even = True  # Başta tüm rakamlar çift varsayımı yap

    for number in s:         # Sayının her karakteri (rakamı) üzerinde dön
        digit = int(number)  # Karakteri tekrar sayıya çevir
        if digit % 2 != 0:   # Eğer rakam tekse (2 ile bölünmüyorsa)
            all_even = False # Artık tüm rakamlar çift değildir
            break            # Kontrolü bırak (tek bir tane bulmak yeterli)

    if all_even:             # Eğer hiç tek rakam bulunmadıysa (hala True ise)
        result.append(i)     # Sayıyı sonuç listesine ekle

print(result)


a = 246

print(a / 10)   # 24.6   → normal bölme (float)
print(a // 10)  # 24     → tamsayı bölme
print(a % 10)   # 6      → kalanı verir (yani son basamak)





###################
# Exercise 5
###################
"""
Write a Python program to guess a number between 1 to 10.
First: Use the predefined code block to create a random number
Second:
The user is prompted to enter a guess. If the guess is wrong a message
"to big" or "to small" is printed to the console and the prompt (user
input) appears again until the guess is correct. If the guess is correct, "Well guessed!" will be printed and the program ends.
Extension:
The number of trials should be prompted as well: "Well done - you have tried it 4 times!"
"""

# Code block to create a random number
from random import randint
random_number = randint(1,10)
# End code block to create a random number

guess_num= int(input("Guess a number between 1 and 10: "))
trials = 1
while guess_num != random_number:
    if random_number > guess_num:
        print("the number is too small")
    else:
        print("the number is too large")
    guess_num = int(input("Next try: "))
    trials += 1
print(f"Well done - you have tried it {trials} times!:"
      f"\nThe number was {guess_num}.")

##########

# Code block to create a random number
from random import randint
random_number = randint(1, 10)
# End code block to create a random number

trials = 0  # Deneme sayısını tutmak için
while True:
    guess_num = int(input("Guess a number between 1 and 10: "))
    trials += 1

    if guess_num < random_number:
        print("The number is too small.")
    elif guess_num > random_number:
        print("The number is too large.")
    else:
        print(f" Well done! You guessed it in {trials} tries!")
        print(f"The number was {random_number}.")
        break  # Tahmin doğruysa döngüden çık

# while True: → sonsuz döngü oluşturur (her zaman devam eder).
# break → koşul sağlandığında döngüyü kırar (burada doğru tahminde).


###################
# Exercise 6
###################
"""
Suppose we wish to draw a Christmas tree.
Example tree - desired height: 8
The result looks like:
     x
    xxx
   xxxxx
  xxxxxxx
 xxxxxxxxx
xxxxxxxxxxx
    xxx
    xxx

Create a program that asks the user for the height of the Christmas tree (trunk included)
and then draws the tree. The height of the trunk is always 2 and the width is 3 in case
the entire height is > 5 and 1 in case the tree is smaller.
"""

height = int(input("What is the height of your tree?: "))

if height > 5:
    trunk_width = 3
    trunk_height = 2
else:
    trunk_width = 1
    trunk_height = 2

# Ağacın yaprak kısmının yüksekliği (trunk hariç)
leaves_height = height - trunk_height

# Ağacın en geniş satır uzunluğu (merkezleme için)
max_width = leaves_height * 2 - 1

stars = 1
for i in range(leaves_height):
    print(("x" * stars).center(max_width))
    stars += 2  # her satırda +2 yıldız

for i in range(trunk_height):
    print(("x" * trunk_width).center(max_width))
