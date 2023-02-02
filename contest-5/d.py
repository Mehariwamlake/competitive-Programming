#!/usr/bin/python3

n= int(input())
line1 = input().split()
nums= list(map(int, line1))
nums.sort()

start = 0
end = 0
isTringle = False

while end <len(nums):
    if((nums[start] + nums[start + 1]) > nums[end]):
        print("YES")
        isTringle = True
        break
    else:
        start += 1
        end += 1

    if(isTringle == False):
        print("NO")
