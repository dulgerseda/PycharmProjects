

#%% Exercise arbitrary key word arguments (**kwargs)
'''
Write a function that accepts an arbitrary number of keyword arguments.
The function should number each keyword-value pair and print it in the following format:
1: keyword -> value
2: keyword -> value
...
n: keyword -> value

a) Test what happens if you pass key word arguments in the format your_function(a=2, b=4)
b) Test what happens if you pass a positional argument
c) Test what happens if you pass key word arguments as a dictionary {"a":2, "b": 4}
d) Use the unpack-operator (**) in the call of the function to pass the keyword arguments
 formatted as a dictionary

Start with the template given below:
'''

#-----pass key word arguments in the format your_function(a=2, b=4)
def print_numbered_kwargs(**kwargs):
    for ind, (key, value) in enumerate(kwargs.items()):
        print(f"{ind}: {key}->{value}")

print_numbered_kwargs(a=2, b=4)
# 0: a->2
# 1: b->4

#----pass a positional argument
a=2
b=4
print_numbered_kwargs(a, b)
# TypeError: print_numbered_kwargs() takes 0 positional arguments but 2 were given

#----pass key word arguments as a dictionary {"a":2, "b": 4}
mydict = {"a": 2, "b": 4}
print_numbered_kwargs(mydict)
# TypeError: print_numbered_kwargs() takes 0 positional arguments but 1 was given


#----unpack-operator (**)
mydict = {"a": 2, "b": 4}
print_numbered_kwargs(**mydict)
# 0: a->2
# 1: b->4




