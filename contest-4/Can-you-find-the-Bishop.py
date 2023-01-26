#!/usr/bin/python3

n = int(input())
while n:
    input()
    f=0
    for i in range(8):
        s=input()
        if s.count('#')==2 and f==0:
            f=1
        elif s.count('#')== 1 and f==1:
            ans = [i+1,s.index("#")+ 1]
            f = 2
    print(ans[0], [1])
    n -= 1