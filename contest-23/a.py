#!/usr/bin/python3

n, s = map(int, input().split())
a= list(map(int, input().split()))

i = 0
s -= 1
while i < s:
    i += a[i]

print("YES" if i == s else "NO")
