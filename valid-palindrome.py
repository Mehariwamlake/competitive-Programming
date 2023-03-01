class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        s = re.sub("[^0-9|^a-z] ", "" ,s.lower())
        l, r = 0, len(s) -1

        while l < r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
            

        return True

        """
        string = ""

        for c in s:
            if c.isalnum():
                string += c.lower()
        return string == string[::-1]
        """