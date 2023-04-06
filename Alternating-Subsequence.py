#!/usr/bin/python

t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	aux = a[0]
	sum = 0

	for num in a:
		if num*aux > 0: 
			aux = max(num, aux)
		else: 
			sum += aux
			aux = num

	sum+=aux
	print(sum)