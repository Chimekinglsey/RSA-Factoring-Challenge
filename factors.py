#!/usr/bin/python3
"""this function reads numbers.txt line by line and compute the first
two numbers that their product equal the number read"""

with open('numbers.txt') as f:
    while f is not None:
        lin = f.readline()
        line = int(lin)
        for  i in range(line):
            for j in range(line):
                if i * j == line:
                #next(if i * j == line)
                    print("{}={}*{}".format(line, j, i))
                    j,i = 0,0
                    break
