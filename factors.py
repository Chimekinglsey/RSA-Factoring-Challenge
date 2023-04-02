#!/usr/bin/python3

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
