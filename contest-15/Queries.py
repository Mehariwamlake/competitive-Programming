n, m = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
lst = []
for i in b:
    l = -1
    r = n
    while r-l > 1:
        mid = (r+l)//2
        if a[mid] <= i:
            l = mid
        else:
            r = mid
    lst.append(r)
print(*lst)