class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        
        l, r = 0, len(s) -1

        while (l<r):
            s[l],s[r] = s[r],s[l]
            l += 1
            r -= 1
        """
        end = len(s) -1
        def recursiv(s, index):
            if index < len(s)/2:
                s[index], s[end-index] = s[end-index], s[index]
                index = index + 1
                recursiv(s,index)
            else:
                return
        recursiv(s, 0)
            
        