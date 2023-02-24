#!/usr/bin/python3

for _ in range(int(input())):
    n,c = input().split()
    n = int(n)
    s= input()
    if c=='g':
        print(0)
    else:
        ans =0
        cp=0
        c_i = -1
        for i in range(n):
            if cp == 0 and s[i] == c:
                c_i = i
                cp = 1
            if s[i] == 'g' and c_i != -1:
                ans = max(ans, i-c_i)
                cp = 0
                c_i = -1

        if c_i != -1:
            for i in range(n):
                if s[i] == 'g':
                    ans =max(ans, n-c_i + 1)
                    break
        print(ans)