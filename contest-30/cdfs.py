from sys import stdin, stdout
 
n = int(input())
a = input()
b = input()
adj = [set() for _ in range(26)]
for i in range(n):
    if a[i] == b[i]:
        continue
    x = ord(a[i]) - ord('a')
    y = ord(b[i]) - ord('a')
    adj[x].add(y)
    adj[y].add(x)
visit = [False] * 26
 
 
def dfs(u, res):
    if visit[u]:
        return
    visit[u] = True
    res.append(u)
    for v in adj[u]:
        if not visit[v]:
            dfs(v, res)
 
ans = []
for u in range(26):
    if not visit[u]:
        res = []
        dfs(u, res)
        for i in range(1, len(res)):
            x = chr(res[0] + ord('a'))
            y = chr(res[i] + ord('a'))
            ans.append((x, y))
 
print(len(ans))
for tu in ans:
    print(*tu)