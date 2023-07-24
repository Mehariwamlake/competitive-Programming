#!/usr/bin/python3

n,m,k = [int(i) for i in input().split()]
if k == 0:
    print(-1)
    exit()
graph = {i+1:{} for i in range(n)}
for _ in range(m):
    u,v,l = [int(i) for i in input().split()]
    graph[u][v] = min(l, graph[u][v] if v in graph[u] else float("inf"))
    graph[v][u] = min(l, graph[v][u] if u in graph[v] else float("inf"))
A = set([int(i) for i in input().split()])
mv = float("inf")
for s in A:
    for nxt in graph[s]:
        if nxt in A:
            continue
        mv = min(mv, graph[s][nxt])
print(mv if mv != float("inf") else -1)