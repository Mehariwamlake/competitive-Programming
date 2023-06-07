#!/usr/bin/python3

s = input()
i = 0
doThat = True

while i<len(s):
    if len(s)>2:
        if s[i:i+3]=='144':
            i+=3
        elif s[i:i+2]=='14':
            i+=2
        elif s[i]=='1':
            i+=1
        else:
            doThat=False
            break

if doThat:
    print('YES')
else:
    print('NO')