t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
 
    freq = {-1: 0, 1: 0}
    for num in nums:
        freq[num] += 1
 
    count = 0
    while freq[-1] > freq[1] or freq[-1] % 2 != 0:
        freq[-1] -= 1
        freq[1] += 1
        count += 1
 
    print(count)