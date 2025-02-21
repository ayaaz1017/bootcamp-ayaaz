from functools import reduce
factorial = reduce(lambda x, y: x * y, range(1, 6))
print(factorial)