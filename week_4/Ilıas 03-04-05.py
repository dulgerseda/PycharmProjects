# enumerate:

x = ["Hello", "World", "Greetings!"]
for e in enumerate(x):
    print(x)
# ['Hello', 'World', 'Greetings!']
# ['Hello', 'World', 'Greetings!']
# ['Hello', 'World', 'Greetings!']

for e in x:
    print(e)
# Hello
# World
# Greetings!

for index, e in enumerate(x):
    print(index, e)
# 0 Hello
# 1 World
# 2 Greetings!

###############################
# Exercise: for/while loop sw3-loop counts
# Calculation of Euler's number e
###############################

# Formula: e = ∑(1 / n!)  from n = 0 to ∞
# In other words:
# e = 1 + 1/1! + 1/2! + 1/3! + 1/4! + ...
# We will calculate it only up to n = 14 for a good approximation.

# Step 1: Calculate the first 11 decimal numbers of e using a for loop
# Step 2: Sum all decimal digits of e up to the 11th position


# Euler sayısını (e) while döngüsüyle hesaplama
# 0'dan 14'e kadar: e = 1/0! + 1/1! + 1/2! + ... + 1/14!

fact = 1
for i in range(1, 15):
    fact *= i
    print (i,fact)


e = 0
fact = 1
for i in range(1, 15):
    if i > 0:
        fact *= i
        e += 1 / fact
    print(i, fact, e)
print("euler sayısı:", e)


x = 0
e = 0
fact = 1
while x < 15:
    if x > 0:
        fact *= x
    e += 1 / fact
    print(x, fact, e)
    x += 1  # bir sonraki adıma geç

##### so:

e = 0
fact = 1
for i in range(1, 15):
    if i > 0:
        fact *= i
        e += 1 / fact
    print(i, fact, e)
print("euler sayısı:", e)
print(f"Euler sayısı: {e:.11f}")


e11 = 1.71828182846
e_str = str(e11)
decimal_part = e_str.split(".")[1]
type(decimal_part)

digit_sum=0
for index, d in enumerate(decimal_part):
# for d in (decimal_part):
      d = int(d)
      # print(d)
      digit_sum += d
print("Euler number decimal number sum:", digit_sum)

# -------------------------------------------------------------------------------------------------
# Loop                               | Value of d             | Explanation
# ---------------------------------- | ---------------------- | -------------------------------
# for d in decimal_part:             | '7', '1', '8', ...     | Returns only each character
# for d in enumerate(decimal_part):  | (0, '7'), (1, '1'), ...| Returns index + character (a tuple)
# --------------------------------------------------------------------------------------------------


# ------------------------------------------------------------
# Exercise: Toasting Guests - sw4
#
# At a party, you want to know how many times guests toast with
# wine before dinner. Assume that each of the n guests has one
# glass and toasts exactly once with every other guest.
#
# Task:
# - Count the total number of toasts using a for-loop and a while-loop.
# - Each pair of guests toasts exactly once.
#
# Hint:
# You can verify your result with the formula:
#     n(n - 1) / 2
# ------------------------------------------------------------


n=5
toast_number=0

for i in range(1,n+1):
    if i==n:
        toast_number  += n-1
        print(i, toast_number)
    elif i== n-1:
        toast_number += n-2
        print(i, toast_number)
    elif i == n-2:
        toast_number += n-3
        print(i, toast_number)
    elif i== n-3:
        toast_number += n-4
        print(i, toast_number)
    else:
        toast_number += n-5
        print(i, toast_number)
print(f"{n} person have {toast_number} toasts")

n = 5
toast_number = 0

for i in range(1, n):
    toast_number += n - i
    print(i, toast_number)

print(f"{n} persons have {toast_number} toasts")

n = 5
toast_number = 0
i = 1

while i < n:
    toast_number += n - i
    print(n, toast_number)
    i += 1

print(f"{n} persons have {toast_number} toasts")

# ------------------------------------------------------------
# Task (Step-by-step, as comments only): sw5-quick slicing
#
# Given string:

#   "$#@|~aslbagjkels nspielbiack ipnzqnmyxrclwqpiofpgwirmvoiupq riepwqdjoi pioack o ocpalsig====%%%**>"

# From the following given string,
# slice every 7th element in reverse order by omitting all heading and tailing sp chs with appropriate start and end positions.
#
# ------------------------------------------------------------

gs = "$#@|~aslbagjkels nspielbiack ipnzqnmyxrclwqpiofpgwirmvoiupq riepwqdjoi pioack o ocpalsig====%%%**>"

cleaned = gs[5:-10]
reversed_cleaned = cleaned[::-1]
print(reversed_cleaned)

result = cleaned[::-7]
print("Every 7th char (reverse order):",
      "\n", result)

result = ""
for i, ch in enumerate(reversed_cleaned):
    if i % 7 == 0:
        result += ch

print("Every 7th char (reverse order):\n", result)

# ------------------------------------------------------------
# Exercise: Quality Measure Mapping sw5-category sorting
# ------------------------------------------------------------
# Given:
#   A list 's' (or 'qm') of quality measures ranging from 0 to 1.
#   The real quality 'q' follows a quadratic function: q = qm ** 2.
#
# Task:
# Create a dictionary 'q_dict' that stores, for each element:
#       - index of q in s
#       - quality measure qm
#       - human-readable category
#
# Use 5 quality categories distributed equally along q:
#       0.0 ≤ q < 0.2  → "bad"
#       0.2 ≤ q < 0.4  → "weak"
#       0.4 ≤ q < 0.6  → "balanced"
#       0.6 ≤ q < 0.8  → "good"
#       0.8 ≤ q ≤ 1.0  → "very good"
#
# Hint:
#   - Start with a linear function (list of qm values)
#   - Compute q = qm ** 2
#   - Then assign the category depending on q
# ------------------------------------------------------------

qm = [0.3, 0.96, 0.7, 0.52, 0.09, 0.68, 0.82, 0.48, 0.33, 0.5,
      0.08, 0.02, 0.75, 0.1, 0.31, 0.22, 0.82, 0.47, 0.11, 0.79,
      0.13, 0.52, 0.34, 0.06, 0.33, 0.39, 0.14, 0.35, 1.0, 0.9]

q = []
for x in qm:
    q.append(x**2)

print(q)

q_dict = {}

for index, value in enumerate(q):
    if value <= 0.2:
        category = "bad"
    elif value <= 0.4:
        category = "weak"
    elif value <= 0.6:
        category = "balanced"
    elif value <= 0.8:
        category = "good"
    else:
        category = "very good"
    q_dict[index]= {'index': index, 'q': round(value, 2), 'category': category}


# Difference:
#
# q_dict[index] → defines the OUTER key of the dictionary (e.g., 0, 1, 2…)
#                 This way, each element is stored separately and the whole list is preserved.
# q_dict = {...} → initializes the dictionary EACH time (only the last value remains!)

# Mac "\" ---> Option +  (*)

print(
    "\n", q_dict[1],
    "\n", q_dict[2],
    "\n", q_dict[3])


for k, v in q_dict.items():
    print(f"{k}: {v}")











