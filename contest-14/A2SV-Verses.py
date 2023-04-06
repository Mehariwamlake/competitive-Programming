n, a, b = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(1, n):
    nums[i] += nums[i]
res = 0
left = 0
dictt = {0:1}
# for i in range(len(nums)): 
#     if nums[i] < a:
#         continue
#     else:
#         while nums[i] - nums[left] > 
    
for i in range(len(nums)):
    # left = 0
    if a <= nums[i] <= b:
        res += 1
    elif nums[i] < a:
        continue

    while left < i :
        if a <=  nums[i] - nums[left] <= b :
            res += i - left 
        left += 1
print(res)