#!/usr/bin/python
from functools import reduce

get_sum = lambda a, b: a + b
get_odd = lambda a: a % 2 != 0
get_even = lambda a: not get_odd(a)
get_multiply = lambda a, b: a * b


def test_a_vs_odd_plus_even():
    a = [1, 2, 3, 4, 5]
    even = list(filter(get_even, a))
    odd = list(filter(get_odd, a))
    sum = reduce(get_sum, a)
    sum_even = reduce(get_sum, even)
    sum_odd = reduce(get_sum, odd)
    multiply = reduce(get_multiply, a)
    multiply_even = reduce(get_multiply, even)
    multiply_odd = reduce(get_multiply, odd)

    print("ARRAY: " + format(a))
    print("ARRAY EVEN: " + format(even))
    print("ARRAY ODD: " + format(odd))
    print("SUM: " + format(sum))
    print("SUM_EVEN: " + format(sum_even))
    print("SUM_ODD: " + format(sum_odd))
    print("MULTIPLY: " + format(multiply))
    print("MULTIPLY_EVEN: " + format(multiply_even))
    print("MULTIPLY_ODD: " + format(multiply_odd))

    even = list(filter(get_even, a))
    odd = list(filter(get_odd, a))
    n = odd + even
    n.sort()
    assert n == a
