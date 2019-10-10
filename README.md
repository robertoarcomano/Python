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

#### Output
```
berto@clevo:~/Desktop/Python$ ./test.py first second third
2 power 3 = 8.0

Params:
0 ./test.py
1 first
2 second
3 third

File first line: #!/usr/bin/python
File chars: 699

string: ./test.py
[0]: .
[1]: /

[2]: t
[3]: e
[4]: s
[5]: t
[6]: .
[7]: p
[8]: y
string[2:5]: test
string[-2:len(string)]: py
```
