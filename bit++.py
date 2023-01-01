n=int(input())

x =0
for i in range(n):
    num = input()
    if '++' in num:
        x+=1
    else:
        x-=1
print(x)
