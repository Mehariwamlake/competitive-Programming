class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        r="abcdefghijklmnopqrstuvwxyz"
        new=""
        n=len(s)
        i = n - 1
        while i>=0:
            if s[i] == '#':
                new = new + r[int(s[i-2:i])-1]
                i -= 3
            else:
                new = new + r[int(s[i])- 1]
                i -= 1
        return new[::-1]