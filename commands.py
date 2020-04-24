#!/usr/bin/python
import os

ls = os.popen("ls -al").read()
print(ls)