def cmp(a, b):
    return (a >= b) - ( a<= b)

a = input()
b = input()
a1 = a.lower()
b1 = b.lower()

print(cmp(a1, b1))