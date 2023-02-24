#!/usr/bin/python3


n, k = map(int,input().split())
s = input()
cnt = 0
for i in range(k):
    if s[i] == "W":
        cnt +=1
print(cnt)
tmp = cnt
for i in range(k, n):
    if s[i-k] =="W":
        tmp -=1
    if s[i] == "W":
        tmp +=1
    
    cnt = min(tmp, cnt)
print(tmp) 
    
print(cnt)