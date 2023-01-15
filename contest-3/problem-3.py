def Solution(Coins):
    G1 = 0
    G2 = 0
    res = 0

    Coins = sorted(Coins)
    for i in Coins:
        G1 += 1

    for i in Coins[::-1]:
        G2 +=1
        res += 1
        if G2 > (G1 / 2):
            break

    return res
if __name__ == "__main__":
    Coins = input()
    Coins_price = list(map(int.input().split()))
    print(Solution(Coins_price))
