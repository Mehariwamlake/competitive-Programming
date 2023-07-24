#!/usr/bin/python3

n = int(input())
parent = [i for i in range(n)]
 
 
def root(node):
    while parent[node] != node:
        parent[node] = parent[parent[node]]
        node = parent[node]
    return node
 
 
def union(a, b):
    root_a = root(a)
    root_b = root(b)
    if parent.count(root_a) > parent.count(root_b):
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
 
 
def find(a, b):
    if root(a) == root(b):
        return True
    return False
 
 
l = list(map(int, input().split()))
q = int(input())
grafo = []
for i in range(q):
    u, v, w = map(int, input().split())
    grafo.append((w, u - 1, v - 1))
 
grafo.sort()
resultado = 0
e = 0
i = 0
associado = [False] * n
while e < n - 1 and i < q:
    w, u, v = grafo[i]
    if not associado[v] and not find(u, v):
        associado[v] = True
        resultado += w
        union(u, v)
        e += 1
    i += 1
if associado.count(False) > 1:
    print(-1)
else:
    print(resultado)
 		  	 	 				  	 			       			