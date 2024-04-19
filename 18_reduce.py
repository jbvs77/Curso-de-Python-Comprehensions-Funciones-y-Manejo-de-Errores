import functools
numbers = [1, 2, 3, 4, 5]

compress = functools.reduce(lambda c, i: c+i, numbers)
print(type(compress))