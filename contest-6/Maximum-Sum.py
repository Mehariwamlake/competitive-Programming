#!/usr/bin/python3

n, m = map(int, input().split())
a = list(map(int, input().split(' ')))

a.sort()
i = 0
j = 0

while m > 0 and a[i]<0:
    j += abs(a[i])
    m -= 1
    i += 1

print(j)