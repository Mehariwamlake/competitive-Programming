#!/usr/bin/python3

nums = input().split("+")
nums.sort()
output=''
for num in nums:
    output = output + num + "+"
print(output[:-1])
