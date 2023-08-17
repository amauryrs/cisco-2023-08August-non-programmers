# # Exercise: Calculator
#
# 1. Write a function, `calc`, that when run asks the user to enter three things:
#     - first number
#     - operator (a string, either `+` or `-`
#     - second number
# 2. Return the value you got from invoking the operator on the numbers.
# 3. Assign the return value from `calc` to the variable `result`, and print it.
#
# Example:
#
#     result = calc()
#     Enter first number: 3
#     Enter operator: +
#     Enter second number: 10
#
#     print(result)
#     13

def calc():
    first = input('First number: ').strip()
    op = input('Enter operator: ').strip()
    second = input('Second number: ').strip()

    first = int(first)
    second = int(second)

    if op == '+':
        return first + second
    elif op == '-':
        return first - second
    else:
        return f'Operator {op} unknown'


print(calc())
