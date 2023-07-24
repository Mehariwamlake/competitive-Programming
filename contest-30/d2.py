#!/usr/bin/python3

def solve():
    n = int(input())
    e = list(map(int, input().split()))
    q = int(input())
    b = []
    for i in range(q):
        x, y, z = map(int, input().split())
        if e[x-1] > e[y-1]:
            b.append((z, x, y))
    b.sort()
    # print(b)
 
    a = [i for i in range(n+1)]
    s = [1 for i in range(n+1)]
    f = [0 for i in range(n+1)]
 
    def root(s):
        while s != a[s]:
            s = a[s]
        return s
    
    def union(x, y, z):
        nonlocal cost
        x = root(x)
        y = root(y)
        if x == y:
            return 
        cost += z
        if s[x] > s[y]:
            a[y] = x
            s[x] += s[y]
        else:
            a[x] = y
            s[y] += s[x]
 
    cost = 0
    
    for c, i, j in b:
        if f[j]:
            continue
        union(i, j, c)
        f[j] = 1
    
    d = set()
    for i in range(1, n+1):
        d.add(root(i))
    if len(d) == 1:
        print(cost)
    else:
        print(-1)
solve()
