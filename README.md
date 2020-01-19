# Python
## Functions
#### Import & Init
```
import sys
import math
import os
n = 1
FILENAME = sys.argv[0]
FIRST_LINE = open(FILENAME,"r").readline().rstrip()
```
#### Functions definition
```
def show(title,string):
    NPAD=50
    global n
    s = "# " + str(n) + ". " + title + "\n"
    s += "*".ljust(NPAD,"*") + "\n"
    s += string
    s += "*".ljust(NPAD,"*") + "\n"
    print(s)
    n += 1

def arguments():
    cmdLine = ""
    arguments = ""
    for i,p in enumerate(sys.argv):
        cmdLine += str(p) + " "
        arguments += "Argument[" + str(i) + "]: " + str(p) + "\n"
    return "Command line: " + cmdLine + "\n" + arguments

def file():
    s = "Filename: " + FILENAME + "\n"
    fileLen = str(os.path.getsize(FILENAME))
    s += "File first line: " + FIRST_LINE + "\n"
    s += "File chars: " + fileLen + "\n"
    return s

def string():
    string = FIRST_LINE
    s = "String: " + string + "\n"
    for i,c in enumerate(string):
        s += "[" + str(i) + "]: " + c + "\n"
    s += "string[2:5]: " + string[2:6] + "\n"
    s += "string[-2:len(string)]: " + string[-2:len(string)] + "\n"
    return s
```
#### Main
```
topics = [
    { "title": "ARGUMENTS", "function": arguments },
    { "title": "FILE", "function": file },
    { "title": "STRING", "function": string },
]

for topic in topics:
    show(topic["title"],topic["function"]())
```

#### Output
```
# 1. ARGUMENTS
**************************************************
Command line: ./test.py
Argument[0]: ./test.py
**************************************************

# 2. FILE
**************************************************
Filename: ./test.py
File first line: #!/usr/bin/python
File chars: 1287
**************************************************

# 3. STRING
**************************************************
String: #!/usr/bin/python
[0]: #
[1]: !
[2]: /
[3]: u
[4]: s
[5]: r
[6]: /
[7]: b
[8]: i
[9]: n
[10]: /
[11]: p
[12]: y
[13]: t
[14]: h
[15]: o
[16]: n
string[2:5]: /usr
string[-2:len(string)]: on
**************************************************
```

## Classes
#### Classes definition
```
class Record:
    name = ""
    def __init__(self,name):
        self.name = name

class Article(Record):
    price = 0
    def __init__(self,name,price):
        super().__init__(name)
        self.price = price
````      
#### Main
````      
user = Record("John")
article = Article("laptop",1000)

print(f"user: {user.name} ")
print(f"article: {article.name} {article.price}")
````      

#### Output
```
user: John
article: laptop 1000
```

## FP
#### Functions definition
```
def sum(a,b):
    return a + b

def multiply(a,b):
    return a * b

def odd(a):
    return False if (a % 2 == 0) else True

def even(a):
    return not odd(a)
````      
#### Main
````      
a = [1,2,3,4,5]
SUM = reduce(sum,a)
SUM_EVEN = reduce(sum,filter(even,a))
SUM_ODD = reduce(sum,filter(odd,a))
MULTIPLY = reduce(multiply,a)
MULTIPLY_EVEN = reduce(multiply,filter(even,a))
MULTIPLY_ODD = reduce(multiply,filter(odd,a))

print(f"ARRAY: {a}")
print(f"ARRAY EVEN: {list(filter(even,a))})")
print(f"ARRAY ODD: {list(filter(odd,a))}")
print(f"SUM: {SUM}")
print(f"SUM_EVEN: {SUM_EVEN}")
print(f"SUM_ODD: {SUM_ODD}")
print(f"MULTIPLY: {MULTIPLY}")
print(f"MULTIPLY_EVEN: {MULTIPLY_EVEN}")
print(f"MULTIPLY_ODD: {MULTIPLY_ODD}")
````      

#### Output
```
ARRAY: [1, 2, 3, 4, 5]
ARRAY EVEN: [2, 4]
ARRAY ODD: [1, 3, 5]
SUM: 15
SUM_EVEN: 6
SUM_ODD: 9
MULTIPLY: 120
MULTIPLY_EVEN: 8
MULTIPLY_ODD: 15
```
