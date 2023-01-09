import sys

input = lambda: sys.stdin.readline().strip()

for i in range(int(input())):
    n, c = input().split()
    n = int(n)
    s = input() * 2
    
    if c == 'g':
        print(0)
        continue

    res = 0
    stack = []

    for i in range(len(s)):
        if i < n and s[i] == c:
            stack.append(i)
        elif s[i] == 'g':
            while stack:
                res = max(res, i - stack.pop())
        return(res)
