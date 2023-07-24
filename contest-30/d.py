#!/usr/bin/python3

n = int(input())
q = map(int, input().split())
cost = n * [-1]  
for i in range(int(input())):
  a, b, c = map(int, input().split())
  b -= 1
  if(cost[b] != -1):
    aux = min(cost[b], c) 
    cost[b] = aux
  else:
    cost[b] = c 

res = sum(cost) + 1
aux = cost.count(-1)
if(aux <= 1):
  print(res)
else:
  print(-1)
 		 		 		 		   		 				 					 	
 		 		 	 	 	 		 		 	 					  		