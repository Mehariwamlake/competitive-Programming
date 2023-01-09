n = int(input())

dic={}
for i in range(n):
    words=str(input())
    if words not in dic:
        dic[words]=words[0:2]+ '... '+words+'?'
for index, val in dic.item():
    print( val)
