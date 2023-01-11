n = int(input())

members = input().split()
bad_a2svian =set(input().split())
good_a2svian = 0
res= 0

for member in members:
    if member not in bad_a2svian:
        charCount = {}
        
        for char in member:
            charCount[char] = charCount.get(char, 0) + 1

        count = charCount[member[0]]
        isGood = True
        for char, i in charCount.item():
            if i != count:
                isGood = False
                break

        if isGood:
            res = res + 1
print(res)
