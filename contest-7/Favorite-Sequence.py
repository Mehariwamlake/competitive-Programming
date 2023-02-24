#!/usr/bin/python3

def poly(n, a):
    for i in range(n):
        j = a[n-1]
        if (i%2==0):
            a.insert((i+1), j)
            a.pop()
    return a
n_pro = int(input())
for problem in range(n_pro):
    n = int(input())
    a = [int(f) for f in input().split()]
    res =poly(n, a)
    print(" ".join([str(f) for f in res]))