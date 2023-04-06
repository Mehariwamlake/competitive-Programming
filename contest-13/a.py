#!/usr/bin/python3
n = input().split('+')
n.sort()

for i in n:
    print('+'.join(i))