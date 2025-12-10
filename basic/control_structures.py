'''
Exercises regarding control structures.
The following exercises should be solved with loops, match case and
if-else conditions ONLY! Comprehensions are NOT part of this exercise.

Author: RCH
Date: 25.11.2024
'''

import random as rd
from operator import length_hint

# given is the following list numbers
nlh = rd.randrange(1,100)
rnd = rd.choices(range(1,100), k=nlh) + rd.choices(range(100,255), k=255-nlh) + [rd.randrange(256, 300)]
rd.shuffle(rnd)
numbers = rnd.copy()

# advanced: do all exercises with the 2d list numbers_ii
numbers_ii = [[rnd.pop() for _ in range(16)] for _ in range(16)]

# Exercise 1:
'''
find the largest number in numbers with for loops and remove it,
if it is at the last position. Do the remove in the else clause of the for loop. WHY???
'''

print(numbers[-1])
max_value = max(numbers)
print(max_value)

for i in range(len(numbers)):
    if numbers[i] == max_value and i == len(numbers) - 1:
        print(max_value)
        break
else:
    numbers.remove(max_value)
    print("removed")

"""Because the else block only runs if the loop finishes without a break,
so removing the element there ensures it’s done only when the largest number 
is not at the last position, making the code safe and logical.,

If no break occurs inside the loop, the else block run.
If a break occurs, the else block does not run.

"""

# Exercise 2:

'''replace all values <100 with 0.'''

for i in range(len(numbers)):
    if numbers[i] < 100:
        numbers[i] = 0

for i, value in enumerate(numbers):
    if value < 100:
        numbers[i] = 0  # replace

print(numbers)

"""We don’t use break here because we need to check and
replace all elements, not stop after the first match."""

# Exercise 3:
'''find the position of the largest number.'''

max_value = max(numbers)
length = len(numbers)

for i, value in enumerate(numbers):
    if value == max_value:
        print(i)
        # break if we add break we just see the first index 64

# Exercise 4:
'''write all numbers != 0 up to the position of the largest number into a new list.'''

new_list = []
pos = numbers.index(max(numbers)) # 64

for value in numbers[:pos]:
    if value != 0:
        new_list.append(value)


new_list = []
max_index = numbers.index(max(numbers))

for i, value in enumerate(numbers):
    if i < max_index and value != 0:
        new_list.append(value)

print(new_list)

# Exercise 5:
'''
count the number of remaining numbers for each decade with match-case statement.
That means, count the number of numbers in ranges:
100 - 125, 126 - 150, 151 - 175, 176 - 200, >200 
'''

count_100_125 = 0
count_126_150 = 0
count_151_175 = 0
count_176_200 = 0
count_over_200 = 0

for n in numbers:
    match n:
        case n if 100 <= n <= 125:
            count_100_125 += 1
        case n if 126 <= n <= 150:
            count_126_150 += 1
        case n if 151 <= n <= 175:
            count_151_175 += 1
        case n if 176 <= n <= 200:
            count_176_200 += 1
        case n if n > 200:
            count_over_200 += 1

print("100–125 :", count_100_125)
print("126–150 :", count_126_150)
print("151–175 :", count_151_175)
print("176–200 :", count_176_200)
print(">200    :", count_over_200)


color = "red"
match color:
    case "red":
        print("Stop!")
    case "yellow":
        print("Get ready!")
    case "green":
        print("Go!")
    case _:
        print("Unknown color")















