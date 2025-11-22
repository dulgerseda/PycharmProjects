'''
Exercise Modules

Fill the parts indicated by "...FILL HERE..." such that the code becomes executable and matches the OUT: statements.

'''

#%% Import entire module
# import string_operations_solution as SO

import string_operations_solution as SO

print(SO.__doc__)

SO.say_something()

print(SO.module_variable)

my_string = 'Hello Universe!'
rev = SO.reverse(my_string)
print(rev)

bi_rev = SO.bi_rev(my_string)
print(bi_rev)

#%% Import specific functions only
from string_operations_solution import reverse
print(reverse("!esrevinU olleH"))

#%% Import specific functions only
from string_operations_solution import reverse, greet_somebody

# greet somebody in reversed order
name = 'Andreas'
print(greet_somebody(reverse(name)))
