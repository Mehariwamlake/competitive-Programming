#!/usr/bin/python3

def solve() -> None:
    n, k = map(int, input().split())
    arr = input()
    arr.sort()
    pres = list(itertools.accumulate(arr, initial=0))
    # print(arr)
 
    if pres[-1] <= k:
        print(0)
        return
 
    ans = pres[-1] - k
    for i in range(n - 1, 0, -1):
        m = n - i
        res = m + (max(pres[i] + arr[0] * m - k, 0) + m) // (m + 1)
        ans = min(ans, res)
 
    print(ans)
 
for _ in range(int(input())):
    solve()
