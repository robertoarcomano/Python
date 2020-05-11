#!/usr/bin/python
import os

import yaml

FILE = "file.yaml"

os.system("rm -f " + FILE)

cmd = """echo \
'\
label1: "new"
list: 
  - item1 
  - item2
record:
  name: John
  surname: Doe  
' > """ + FILE
os.system(cmd)

list_items = []
try:
    with open(FILE) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        list_items = data['list']
        record = data['record']
except:
    pass
print("list:")
for i, item in enumerate(list_items):
    print(i, item)
print("record:")
for item in record:
    print(item + ": " + record[item])
print("label: " + data["label"] if "label" in data else "no")