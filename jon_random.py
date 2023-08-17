import random
numbers = []
for counter in range(10):  # 10 times
    n = random.randint(0, 100)  # get a random number
    numbers.append(n)  # add n to the end of the numbers
print(numbers)

