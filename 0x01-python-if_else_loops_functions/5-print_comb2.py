#!/usr/bin/python3
for i in range(0, 100):
    if (i < 10):
        print("0{}, ".format(i), end="")
        continue
    print("{}".format(i), end="\n" if i == 99 else ", ")
