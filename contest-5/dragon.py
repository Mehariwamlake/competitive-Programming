def solve(s, dragons):
    dragons.sort()
    for strength, bonus in dragons:
        if s <= strength:
            return "NO"
        s += bonus
    return "YES"
s, n = map(int, input().split())
dragons = []
for i in range(n):
    strength, bonus = map(int, input().split())
    dragons.append((strength, bonus))
ans = solve(s, dragons)
print(ans)