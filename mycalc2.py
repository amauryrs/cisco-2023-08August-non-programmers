def calc(first, op, second):

    if op == '+':
        return first + second
    elif op == '-':
        return first - second
    else:
        return f'Operator {op} unknown'


print(calc(10, '+', 3))
print(calc(12, '-', 3))
print(calc(10, '*', 3))
