def dfs(cell):
	global d, vis
	if cell in vis:
		return
	vis.add(cell)
	for eachCell in d[cell]:
		dfs(eachCell)
		
m,n = map(int,input().split())
if (n + 1) != m:
	print('no')
else:
	d = {}
	for __ in range(n):
		x, y = map(int,input().split())
		if x not in d:
			d[x] = []
		if y not in d:
			d[y] = []
		d[x].append(y)
		d[y].append(x)
	vis = set()
	dfs(1)
	total = set(range(1,m+1))
	if vis == total:
		print('yes')
	else:
		print('no')
		 		   	   		  		      			