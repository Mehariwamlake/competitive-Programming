#!/usr/bin/python3

n, d = map(int, input().split())
s = sorted(list(map(int, input().split())), reverse=True)

x = 0
ans = 0
i = 0
while n > 0:
    x += s[i]
    if x > d:
        ans += 1
        x = 0
        i += 1
    n -= 1
    
print(ans)