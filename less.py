#!/usr/bin/python3

arr = list(map(int, input().split()))
lst = list(map(int, input().split()))

lst.sort()
# print(lst)

k = arr[1]

def calc(k, lst):
    if k == 0:
        if lst[0] > 1:
            return 1
        return -1
    if k < len(lst) and lst[k - 1] == lst[k]:
            return -1
    return lst[k-1]

print(calc(k, lst))