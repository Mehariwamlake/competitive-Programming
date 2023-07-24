n, edges = [int(x) for x in input().split()]

adj_list = [[] for _ in range(n)]
for _ in range(edges):
    left, right = [int(x)-1 for x in input().split()]

    adj_list[left].append(right)
    adj_list[right].append(left)

t: int = 0
o: int = 0
nm1: int = 0

for connections in adj_list:
    if len(connections) == 1:
        o += 1
    elif len(connections) == 2:
        t += 1
    elif len(connections) == n-1:
        nm1 += 1


print(('bus' if t == n - 2 and o == 2 else ('star' if nm1 == 1 and o == n - 1 else ('ring' if t == n else 'unknown'))) + ' topology')