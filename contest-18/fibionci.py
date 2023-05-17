#!/usr/bin/python3

n = int(input())
a = [1,1]
for i in range(n-1):
    a.append(sum(a[-2:]))
print(a[-1])