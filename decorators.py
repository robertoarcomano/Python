#!/usr/bin/python


def log(fun):
    def internal(cmd):
        print("- PRE -")
        fun(cmd)
        print("- POST -")
        print()

    return internal


@log
def execute(cmd):
    print("Executing " + cmd)


for i in range(1, 11):
    execute("cmd_" + str(i))
