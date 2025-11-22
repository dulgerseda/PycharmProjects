########################
# TASK 1: if, else, elif
########################

"""
Create a simple program in which three whole numbers (potentially negative!) are read in from
the keyboard and afterwards get displayed on the screen in ascending order.
Use nested if-statements for order determination (i.e. no built-in- 'sort' function).
"""

# numbers = input("Enter three integers a b c separated by spaces (e.g. -5 0 12): ")
# print(f"numbers are {numbers}")

# sorted_numbers = sorted(numbers.split())
# print(sorted_numbers)

a = int( input( "Input 'a': "))
b = int( input( "Input 'b': " ))
c = int( input( "Input 'c': " ))

if a < b:
    if b < c:
        print(a,b,c)
    else:
        if a < c:
            print(a,c,b)
        else:
            print(c,a,b)

else:
    if b > c:
        print(c,b,a)
    else:
        if a > c:
            print(b,c,a)
        else:
            print(b,a,c)



########################
# Task 2a: if, and-Operator, or-Operator
########################

"""
Assumption: The int variables a, b and c are declared and initialized.

Define a conditional expression "EXPR" in such a way that the body of the expression

if EXPR:
    print("condition fulfilled")

is only carried out if:
a is greater than b OR a is less than half of b OR the sum of a and c is greater than b.


Check your result:
a=1, b=2, c=2 -> True
a=1, b=2, c=1 -> False
"""

a=1
b=2
c=2


if a>b or a<(b/2) or (a+c) > b:
    print("condition fulfilled")


########################
# Task 2b: if, and-Operator, or-Operator
########################

"""
Assumption: The int variables a, b and c are declared and initialized.

Define a conditional expression "EXPR" in such a way that the body of the expression

if EXPR:
    print("condition fulfilled")

is only carried out if:
half of the number a is an odd number 
OR the subtraction of the numbers b and c results in an even number 
OR both 
a and b and also b and c have different values.

Check your result:
a=6, b=2, c=0 => True
a=5, b=2, c=1 => True
a=5, b=5, c=2 => False
"""

a=5
b=5
c=2

# if ((a/2)%2 == 0 or (b-c)%2 == 0 or (a != b) and (b != c)):
#   print("condition fulfilled")

if ((a % 2 == 0 and (a // 2) % 2 == 1) or (b-c)%2 == 0 or (a != b) and (b != c)):
    print("condition fulfilled")


# 1. Normal division (/) → her zaman float döner
print(6 / 2)   # 3.0  (float)
print(7 / 2)   # 3.5
print(-7 / 2)  # -3.5

# 2. Floor division (//) → tam kısmı alır, aşağı yuvarlar
print(6 // 2)   # 3   (int)
print(7 // 2)   # 3   (ondalık kısmı atar)
print(-7 // 2)  # -4  (dikkat! aşağı yuvarlıyor, -3 değil -4 çıkar)

# half of the number a is odd” derken, biz “a/2 tam sayı çıkmalı ve tek olmalı” diyoruz, O yüzden a // 2


a=6
b=2
c=0

half_is_odd = (a % 2 == 0 and (a // 2) % 2 == 1)
diff_is_even = ((b - c) % 2 == 0)
both_diff    = (a != b and b != c)

if half_is_odd or diff_is_even or both_diff:
    print("True")
else:
    print("False")
