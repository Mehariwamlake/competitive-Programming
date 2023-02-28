#!/usr/bin/python3

for i in range(int(input())):
    n = int(input())
    s = input()
    fas = s[0]
    las = s[-1]
    if fas == las:
        print(lene(s))
    else:
        xas = s 
        while(len(xas)>2):
            xas =xas[1:len(xas)-1]
            fas=xas[0]
            las=xas[-1]
            if fas == las:
                break
        fas = xas[0]
        las = xas[-1]
        if fas != las:
            print(0)
        else:
            print(len(xas))