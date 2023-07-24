n = int(input())
m = int(input())
L = []
for i in range(n):
    L.append(int(input()))

maxK = max(L) + m  
m1 = m 
L.sort()
n2 = max(L)
for i in L:
    m1 -= (n2-i)

if m1 <= 0:
    print(n2,end = " ")
else:
    t1 = m1//n 
    if m1%n != 0:
        t1 += 1 
    print(n2 + t1,end = " ")

print(maxK)