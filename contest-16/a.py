#!/usr/bin/python3

n=int(input())
s=input()
ans=0
for i in s:
          if i=='+':
              ans+=1
          else:
              ans=max(ans-1,0)
print(ans)