#!/usr/bin/python3

for i in range(int(input())):
    s = sorted(input())

    if s[0] == s[-1]:
        print(-1)
    else:
        print("".join(s))