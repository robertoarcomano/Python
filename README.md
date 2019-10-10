# Python
## Simple example source file for Python
#### Import
```
import sys;
import math;
```
#### Functions
```
def power(base,exp):
    return math.pow(base,exp);

def params():
    s = "Params: \n"
    for i,p in enumerate(sys.argv):
        s += str(i) + " " + str(p) + "\n"
    return s

def file():
    f = open("test.py","r")
    return "File first line: " + f.readline() + "File chars: " + str(len(f.read()))

def string(string):
    s = "string: " + string + "\n"
    for i,c in enumerate(string):
        s += "[" + str(i) + "]: " + c + "\n"
    s += "string[2:5]: " + string[2:6] + "\n"
    s += "string[-2:len(string)]: " + string[-2:len(string)] + "\n"
    return s
```

#### Main
```
print("2 power 3 = " + str(power(2,3)))
print
print params()
print file()
print
print string(sys.argv[0])
```
