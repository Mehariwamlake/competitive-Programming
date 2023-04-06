#!/usr/bin/python3

test = int(input())

for i in range(test):
    n, m = map(int, input().split())
    div = list(map(int, input().split()))
    div.sort(reverse=True)
    s = 2
    ans = 0


    for num in div:
        if s >= n:
            break
        else:
            s += num - 1
            ans += 1
    if s < n:
        ans = -1
        
    print(ans)