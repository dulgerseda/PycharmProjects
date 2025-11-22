
a = list(range(10))

b = list(range(10, -10, -1))

cut1 = b[0:3]
cut2 = b[0:6:2]
r = b[::-1]

for e in b:
    e = e + 10
    print (e)
else:
    print("end")


for e in b:
    for j in b:
        x = j * e
        print (x)


x,y = [1,2]

for e in range(10):
    print ("Hello World")


a = [1,2,3,4,5,10,17]
for e in a[::3]:
    print (e)

for e in a:
    if e % 2 == 0:
       print(e)

# while => as long as
x = 12
while x < 10:
    print (x)
    x = x * 2
else:
    print("end")
print (x)


x = 0
while x % 2:
    print (x)
    x = x + 1
else:
    print("what?")

print("-----------")

x = 0
while x % 2 == 0:
    print (x)
    x = x + 1
else:
    print("what?")



### break/continue/pass

x = [1,2,3]

for e in x:
    pass

x = 1
while True:
    x = x + 1
    if x == 2:
        break
print("loop end!")

### enumerate

x = ["Hello", "World", "Greetings!"]
for e in x:
    print(e)

x[0]
x[:2]

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
