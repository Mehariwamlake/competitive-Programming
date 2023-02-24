#!/usr/bin/python3

a = int(input())
b = list(map(int, input().split()))
b.sort()
i = 0

while (i<a//2):
    print(b[i], b[-i-1], end= ' ')
    i += 1
if a % 2:
    print(b[a//2])