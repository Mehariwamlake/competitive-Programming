#!/usr/bin/python3

n = int(input())
nums = [int(x) for x in input().split()]
ans = 0
l = 0
r = 0
while(r < n):
    l = r
    while (r < n -1 and nums[r+1] >= nums[r]):
        r += 1
    ans = max(ans , r-l +1)
    r += 1
print(ans)