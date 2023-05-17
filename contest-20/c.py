#!/usr/bin/python3
for i in range(int(input())):
    n, x = input(), 0
    for j in map(int, input().split()):
        x = x | j

    print(x)