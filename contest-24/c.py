n = int(input())
arr = list(map(int, input().split()))
s = input()

ans = []
temp = []
for i in range(len(arr) - 1):
  temp.append(arr[i])
  if s[i] == '0':
    temp.sort()
    # print(temp)
    ans.extend(temp)
    temp = []

temp.append(arr[-1])
temp.sort()
# print(temp)
ans.extend(temp)

print('YES' if ans == sorted(arr) else 'NO')