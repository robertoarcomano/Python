#!/usr/bin/python

a = []
for i in range(0, 10):
    a.append(i)
print(a)

b = [i for i in range(0, 10)]
print(b)

c = (i for i in range(1,10))
for i in c:
    print(i)
