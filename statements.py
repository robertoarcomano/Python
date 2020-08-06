#!/usr/bin/python

conditions = [True, False, True, True]

if all(conditions):
    print("all")
elif any(conditions):
    print("any")
else:
    print("else")
for c in conditions:
    print(c)
for i in range(0, len(conditions)):
    print(i, conditions[i])
i = 0
while i < len(conditions):
    print(i, conditions[i])
    i += 1
else:
    i = 0
