#!/usr/bin/python
import os
import yaml

FILE="file.yaml"

os.system("rm -f " + FILE)

cmd = """echo 'list: 
  - item1 
  - item2' > """ + FILE
os.system(cmd)

list_items = []
try:
    with open(FILE) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        list_items = data['list']
except:
    pass
for item in list_items:
    print(item)
