from heapq import heappush,heappop
for _ in range(int(input())):
	n=input()
	a=list(map(int,input().split()))
	q=[];ans=[];x=1;
	for c in a:
		if c!=0:heappush(q,(-c,x))
		x+=1
	while(len(q)>1):
		c,x=heappop(q)
		d,y=heappop(q)
		if c+1!=0:heappush(q,(c+1,x))
		if d+1!=0:heappush(q,(d+1,y))
		ans+=(x,y),
	print(len(ans))
	for i,j in ans:print(i,j) 