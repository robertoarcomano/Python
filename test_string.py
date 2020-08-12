#!/usr/bin/python
from past.builtins import reduce

arr = ["item" + str(item) for item in range(1, 11)]
print("arr created by comprehension: " + format(arr))

string = "|".join(arr)
print("string created by join: " + string)
item = "item3"
print("search " + item + " in string using index: found: " + str(item in string) + " position: " + str(string.index(item)))

arr = string.split("|")
print("arr created by split: " + format(arr))
print("search " + item + " in arr using 'in': found: " + str(item in arr) + " position: " + str(arr.index(item)))

