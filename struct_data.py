#!/usr/bin/python

tuple1 = (1, 2, 3)
list1 = [1, "cool", 3]
dict1 = {
    "first": 1,
    "second": 2,
    "third": 3
}
json1 = {
    "data": [
        {
            "id": 1,
            "name": "name1"
        },
        {
            "id": 2,
            "name": "name2"
        },
    ]
}
print("tuple: " + format(tuple1))
for i, v in enumerate(tuple1):
    print(format(i) + ": " + format(v))
print()

print("list: " + format(list1))
for i, v in enumerate(list1):
    print(format(i) + ": " + format(v))
print()

print("dictionary: " + format(dict1))
for k in dict1:
    print(k + ": " + format(dict1[k]))
print()

print("json: " + format(json1))
for i, v in enumerate(json1):
    print(format(v))
    for j, w in enumerate(json1[v]):
        print("  " + format(j))
        for k, x in enumerate(json1[v][j]):
            print("  " + "  " + format(x) + ": " + format(json1[v][j][x]))

