#!/usr/bin/python3

test = int(input())
for _ in range(test):
    w , s, f = map(int, input().split())

    temp1 = (f + 4) * s
    temp2 = f * w + (4 - f) * s
    temp3 = w * 4
    print(min(temp2, temp1, temp3))