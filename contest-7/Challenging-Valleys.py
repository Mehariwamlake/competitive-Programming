#!/usr/bin/python3

n = int(input().split())
a = []
for i in range(n):
    a.append(n)

l, r = 0, n-1
while l<r:
    if a[l] >= a[l+1]:
        l += 1
    elif r > 0 and a[r] >= a[r-1]:
        r -=1
    else:
        print('NO')
print('YES')

