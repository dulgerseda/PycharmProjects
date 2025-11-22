# main.py

#Absolute import
from week_10.mymodules import mymodule as MM
from week_6.maindeneme import myadder

print("Value from mymodule:", MM.myvar)

a = 3
b = 5
result = MM.intsum(a, b)
print("Sum result from mymodule:", result)

print("From week_6.maindeneme func:", myadder(3, 5))















