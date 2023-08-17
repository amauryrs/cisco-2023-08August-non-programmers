# # Exercise: 10 random numbers
#
# 1. Define an empty list, `numbers`.
# 2. Call `random.randint` 10 times, asking for a random integer between 0 and 100.
# 3. Add each of these numbers to `numbers`.
# 4. Print `numbers`.
#
# Do this in PyCharm!
#
# Hints:
# - You'll need to import the module
# - Remember that you can use `range` to iterate a number of times
# - Use `list.append` to add to an existing list.

import random

numbers = []

for index in range(10):
    n = random.randint(0, 100)   # get a random number
    numbers.append(n)            # add n to the end of numbers

print(numbers)


