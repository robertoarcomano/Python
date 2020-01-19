#!/usr/bin/python
from functools import reduce

def sum(a,b):
    return a + b

def multiply(a,b):
    return a * b

def odd(a):
    return False if (a % 2 == 0) else True

def even(a):
    return not odd(a)

a = [1,2,3,4,5]
SUM = reduce(sum,a)
SUM_EVEN = reduce(sum,filter(even,a))
SUM_ODD = reduce(sum,filter(odd,a))
MULTIPLY = reduce(multiply,a)
MULTIPLY_EVEN = reduce(multiply,filter(even,a))
MULTIPLY_ODD = reduce(multiply,filter(odd,a))

print(f"ARRAY: {a}")
print(f"ARRAY EVEN: {list(filter(even,a))}")
print(f"ARRAY ODD: {list(filter(odd,a))}")
print(f"SUM: {SUM}")
print(f"SUM_EVEN: {SUM_EVEN}")
print(f"SUM_ODD: {SUM_ODD}")
print(f"MULTIPLY: {MULTIPLY}")
print(f"MULTIPLY_EVEN: {MULTIPLY_EVEN}")
print(f"MULTIPLY_ODD: {MULTIPLY_ODD}")
