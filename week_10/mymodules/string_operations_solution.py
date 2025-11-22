'''
Collection of methods to manipulate strings.
'''

module_variable = 'Hello'

def reverse(string):
    return string[::-1]

def bi_rev(string):
    return string[::-2]

def say_something():
    print(module_variable)

def greet_somebody(name):
    return "Hello {}".format(name)
