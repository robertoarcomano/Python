#!/usr/bin/python
import threading

global_var = 0
num_thread = 8


class myThread(threading.Thread):
    def __init__(self, n):
        self.internal = n
        super().__init__()
        global global_var
        print(n, global_var)
        print(n, "++")
        global_var += n
        print(n, global_var)


threads = list()
for i in range(0, num_thread):
    threads.append(myThread(i))

for i in range(0, num_thread):
    threads[i].start()

for i in range(0, num_thread):
    threads[i].join()

for i in range(0, num_thread):
    print(threads[i].internal)
