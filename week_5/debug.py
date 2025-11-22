
a = 3
b = 5
a = 6
for elem in range(10):
    if elem > 5:
        print(elem)

print("--")
print(a)
print(b)

# Debugging Demonstration: Understanding Breakpoints

x = 2
y = 3
z = x + y     # (1)

print("Before the breakpoint")  # (2)

# You can put a breakpoint on the next line
result = z * 2                  # (3)

print("After the breakpoint")   # (4)
print("Result:", result)        # (5)
