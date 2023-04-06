n, k = map(int, input().split())
ans = -1000000000
for i in range(n):
    f, t = [int(x) for x in input().split()]
    if t > k:
        joy = f - (t - k)
    else:
        joy = f
    if ans < joy: ans = joy
print(ans)