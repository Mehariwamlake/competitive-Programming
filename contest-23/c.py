n,m=map(int,input().split())
c=list(map(int,input().split()))

from collections import defaultdict

adj=defaultdict(list)

vis= [0 for i in range(n+1)]

for i in range(m):
  u,v=map(int,input().split())
  adj[u].append(v)
  adj[v].append(u)

ans=0  

def DFS(x):
	z = float("inf")
	stack = [x]
	while len(stack):
		temp = stack.pop()
		vis[temp] = 1
		z = min(z,c[temp-1])
		for j in adj[temp]:
			if not vis[j]:
				stack.append(j)
	return z
	

for i in range(1,n+1):
  if not vis[i]:
    ans+=DFS(i)

print(ans)
	  	 					 				    	  	 		  	 	