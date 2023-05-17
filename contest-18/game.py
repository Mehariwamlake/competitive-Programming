#!/usr/bin/python3

def solve():
    n = int(input())
    array_dimension = []
    array_sum_x = {}
    array_sum_y = {}
    for i in range(n):
        temp = list(map(int,input().split()))
        array_sum_x[i] = sum(temp)
        array_dimension.append(temp)
    for i in range(n):
        current_sum = 0
        for j in range(n):
            current_sum += array_dimension[j][i]
        array_sum_y[i] = current_sum
    total_win = 0
    for i in range(n):
        for j in range(n):
            if array_sum_x[i] < array_sum_y[j]:
                total_win += 1
    print(total_win)



if __name__ == "__main__":
    solve()