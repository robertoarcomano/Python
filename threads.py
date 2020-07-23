#!/usr/bin/python
import threading

global_var = 0
num_thread = 8

ret_list = list()


def start(n, ret):
    global global_var
    print(n, global_var)
    print(n, "++")
    global_var += n
    print(n, global_var)
    ret.append({"self": 1, "n": n})


threads = list()
for i in range(0, num_thread):
    threads.append(threading.Thread(target=start, args=(i, ret_list)))

for i in range(0, num_thread):
    threads[i].start()

for i in range(0, num_thread):
    threads[i].join()

for i in range(0, num_thread):
    print(threads[i])

print(ret_list)
