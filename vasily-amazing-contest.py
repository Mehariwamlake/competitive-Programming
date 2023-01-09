
n= int(input())
s= list(map(int, input().split()))

more = s[0]
less = s[0]
count = 0
for i in range(len(s)):
    if s[i] > more:
        more = s[i]
        count +=1
    if less > s[i]:
        less = s[i]
        count +=1
print(count)