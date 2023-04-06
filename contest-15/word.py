#!/usr/bin/python3

n = input()
l = len(n)

counter = 0

for i in n:
    if i >= 'a' and i<='z':
        counter += 1

if counter >= (l/2):
    print(n.lower())
else:
    print(n.upper())