#!/usr/bin/python3
    
def minDeletionSize(self, strs: list[str]) -> int:
    strs = ["cba","daf","ghi"]    
    n = len(strs)
    m = len(strs[0])
    output = 0

    for col in range(m):
        for row in range(n - 1):
            if strs[row][col] > strs[row + 1][col]:
                output += 1
                break
    print(strs[row][col],strs[row+1][col])
    return output