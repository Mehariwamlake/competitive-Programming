#!/usr/bin/python3

n = int(input())

for i in range(n):
    a,b = map(int, input().split())
    c,d = map(int, input().split())
    if max(a,b)==max(c,d) and (min(a,b)+ min(c,d))== max(a,b):
        print('Yes')
    else:
        print("No")
    

