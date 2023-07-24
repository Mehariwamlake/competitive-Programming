#!/usr/bin/python3

def make_divisible(arr):
    n = len(arr)
    arr.sort()
    ops = 0
    for i in range(n-1):
        a, b = arr[i], arr[i+1]
        if b % a != 0:
            r = a - (b % a)
            ops += 1
            arr[i+1] += r
            arr[i] += r*(b//a)
    return ops

    arr = [2 ,3, 5, 5]


for s in[*open(0)][2::2]:
 print(len(a:=s.split()));i=0
 for x in map(int,a):i+=1;print(i,2**len(f'{x:b}')-x)
				 			    	 	  		      	