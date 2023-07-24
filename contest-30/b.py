#!/usr/bin/python3

n = int(input())


mappings = {}

for i in range(n):
    old, new = input().split()
    
    if old in mappings:
        mappings[new] = mappings[old]
        del mappings[old]
    else:
        mappings[new] = old

print(len(mappings))
for new, old in mappings.items():
    print(old, new)

	     	   		 		  	    	 	 		 	