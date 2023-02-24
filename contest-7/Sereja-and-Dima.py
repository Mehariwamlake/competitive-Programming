#!/usr/bin/python3

n = int(input())
lista = list(map(int, input().split()))
p1 = 0
p2 = 0

cont = 1
while lista:
    maxi = max(lista[0], lista[-1])
    if cont&1:
        p1 += maxi
    else:
        p2 += maxi

    if maxi == lista[-1]:
        lista.pop()
    else:
        lista.pop(0)

    cont += 1
print(p1, p2)