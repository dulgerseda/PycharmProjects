from traceback import print_list

a = 2


def myfunc():
    b = 4
    print("hello")
    print(b)
    print(a)


myfunc()
print(a)

a = 7
for i in range(a):
    print(i)

print("---")
print(i)

#----------------

cnt = 1


def myfunc():
    # global cnt : you can reach the global value while using a func
    cnt = 10
    cnt += 1
    print(cnt)


myfunc()
print(cnt)


#----------------

def myfunc():
    print("enterinng the function")

    def inner_func():
        print("enterinng the function")

    print("half way")

    inner_func()
    print("my func done")


myfunc()

#----------------

cnt = 1


def myfunc():
    cnt = 2

    def inner_func():
        nonlocal cnt  # nonlocal is go up until find the variable
        cnt = 3

    inner_func()
    print("my func done")


myfunc()
print(cnt)

#----------------

a = 3


def myfunc():
    print(a)


myfunc()

#----------------

clist = [1, 2, 3]


def myfunc(clist):
    print(clist)
    clist[2] = 99
    print(clist)


myfunc(clist)
print(clist)


#----------------

def mysum(*args):
    sum_res = 0
    for i in args:
        sum_res = sum_res + i
    return sum_res

res = mysum(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(res)

#----------------

mystring="hello world"
def myfunc():
    print(mystring)
    return mystring.upper()
a = myfunc()
print(a)

#----------------SW07:
# Given a list with an arbitrary number of nested sublists.
# The goal of this exercise is to write a recursive function which returns the position of an
# element in the given list in a specific format.
# Write a recursive function that returns the position of a specific element e
# as a sequence of numbers. Each number in your sequence refers to the position of
# the sublist containing the element somewhere in its sub-structure, relative to its parent list.
# The last number contains the position of the element in the list which contains the actual element.
# The function returns None if the element is not in the list nor in any sublist.
# Note:
# using the function type(x) in a boolean statement like type(x)==list you can check
# if a list element x is of type list.


myList = [1, 2, 3, [11, 22, 33], 4, [44, 55, [111, 222], 66, 77], 5, 6, [88], 7]

def findValue(l, e):
    p_list = []
    for index, i in enumerate(l):
        if i == e:
            p_list.append([index])
        elif type(i) == list:
            result = findValue(i, e)
            for r in result:
                p_list.append([index] + r)
    return p_list

print(findValue(myList, 222))


myList = [1, 2, 3, [11, 22, 33], 4, [44, 55, [111, 222], 66, 77], 5, 6, [88], 7]
print(findValue(myList, 222))

# output:
[5, 2, 1]




