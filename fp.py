#!/usr/bin/python
# from functools import reduce

get_sum = lambda a, b: a + b
get_odd = lambda a: a % 2 != 0
get_even = lambda a: not get_odd(a)
get_multiply = lambda a, b: a * b

# a = [1, 2, 3, 4, 5]
# SUM = reduce(sum, a)
# SUM_EVEN = reduce(sum, filter(even, a))
# SUM_ODD = reduce(sum, filter(odd, a))
# MULTIPLY = reduce(multiply, a)
# MULTIPLY_EVEN = reduce(multiply, filter(even, a))
# MULTIPLY_ODD = reduce(multiply, filter(odd, a))
#
# print("ARRAY: " + str(a))
# print("ARRAY EVEN: " + str(filter(even, a)))
# print("ARRAY ODD: " + str(filter(odd, a)))
# print("SUM: " + str(SUM))
# print("SUM_EVEN: " + str(SUM_EVEN))
# print("SUM_ODD: " + str(SUM_ODD))
# print("MULTIPLY: " + str(MULTIPLY))
# print("MULTIPLY_EVEN: " + str(MULTIPLY_EVEN))
# print("MULTIPLY_ODD: " + str(MULTIPLY_ODD))
