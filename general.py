#!/usr/bin/python
import sys
import math
import os

n = 1
FILENAME = sys.argv[0]
FIRST_LINE = open(FILENAME, "r").readline().rstrip()


def show(title, string):
    NPAD = 50
    global n
    s = "# " + str(n) + ". " + title + "\n"
    s += "*".ljust(NPAD, "*") + "\n"
    s += string
    s += "*".ljust(NPAD, "*") + "\n"
    print(s)
    n += 1


def arguments():
    cmdLine = ""
    arguments = ""
    for i, p in enumerate(sys.argv):
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
    for i, c in enumerate(string):
        s += "[" + str(i) + "]: " + c + "\n"
    s += "string[2:5]: " + string[2:6] + "\n"
    s += "string[-2:len(string)]: " + string[-2:len(string)] + "\n"
    return s


topics = [
    {"title": "ARGUMENTS", "function": arguments},
    {"title": "FILE", "function": file},
    {"title": "STRING", "function": string},
]

for topic in topics:
    show(topic["title"], topic["function"]())
