from collections import Counter
 
t = int(input())
 
for _ in range(t):
    n, k = map(int, input().split(" "))
    s = input()
    t = input()
 
    if(Counter(s) != Counter(t)):
        print("NO")
        continue
 
    answer = "YES"
    for i in range(n):
        if(s[i] != t[i]):
            if(i-k < 0 and i+k > n-1):
                answer = "NO"
                break
 
    print(answer)