#!/usr/bin/python

c = (i for i in range(1, 1000))
n = sum(1 for dummy in c)
print(n)
