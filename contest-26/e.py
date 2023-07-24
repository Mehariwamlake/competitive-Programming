n, k , q = list(map(int, input().split()))

i =0
nl = [0]*200002

while(i< n ):
    l, r =  list(map(int, input().split()))
    nl[l]+=1
    nl[r+1]-=1
    i+=1

for i2 in range (1,200002):
    nl[i2] = nl[i2] + nl[i2-1]


arr = [0]*200002

for i2 in range (1,200002):
    if (nl[i2] >= k):
        arr[i2] = 1

for i2 in range (1, 200002):
    arr[i2] = arr[i2] + arr[i2-1]

j= 0  

while(j< q):
    a2, b2 =  list(map(int, input().split()))

    print(arr[b2]- arr[a2-1])
    j+=1