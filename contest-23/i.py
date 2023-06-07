n,d=map(int,input().split())
a=input()
x=0
r=0
while x!=n-1:
  y=a[:x+d+1].rfind('1')
  if y==x:
    r=-1
    break
  else:x=y
  r+=1
print(r)