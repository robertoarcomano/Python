#!/usr/bin/python
import threading
import time

global_var = 0
num_thread = 8


def start(n):
    global global_var
    print(n, global_var)
    print(n, "++")
    global_var += n
    print(n, global_var)


threads = list()
for i in range(0, num_thread):
    threads.append(threading.Thread(target=start, args=(i,)))

for i in range(0, num_thread):
    threads[i].start()

for i in range(0, num_thread):
    threads[i].join()
