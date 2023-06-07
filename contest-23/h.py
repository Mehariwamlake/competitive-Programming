#!/usr/bin/python3

n, m = map(int, input().split())
result = 0

while n< m:
    if m%2 == 0:
        m //= 2

    else:
        m += 1

    result += 1
result += n - m
print(result)