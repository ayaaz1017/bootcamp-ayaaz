
import functools

sum_of_squares = functools.reduce(lambda x, y: x + y, [x**2 for x in range(1, 11)])
print(sum_of_squares)