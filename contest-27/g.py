from collections import defaultdict

set1 = []
seto = set()
vis = defaultdict(int)
dep = defaultdict(int)
valid = False

def calcdep(node, par, adjlist):
    if par != -1:
        dep[node] = dep[par] + 1
    for c in adjlist[node]:
        if c == par:
            continue
        else:
            calcdep(c, node, adjlist)

def dfs(node, count, adjlist):
    vis[node] = 1
    if len(seto) == count:
        global valid
        valid = True
    for c in adjlist[node]:
        if not vis[c]:
            if c in seto:
                dfs(c, count+1, adjlist)
        else:
            dfs(c, count, adjlist)

def vectorofPrimeFactors(n):
    i = 2
    while i*i <= n:
        while n%i == 0:
            set1.append(i)
            n = n//i
        i += 1
    if n > 1:
        set1.append(n)

n = int(input())
adjlist = defaultdict(list)
for i in range(2, n+1):
    a, b = map(int, input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)

calcdep(1, -1, adjlist)
q = int(input())
seto.clear()
while q > 0:
    seto.clear()
    vis.clear()
    q -= 1
    k = int(input())
    seto = set(map(int, input().split()))
    valid = False
    dfs(1, 0, adjlist)
    if valid:
        print("YES")
    else:
        print("NO")
