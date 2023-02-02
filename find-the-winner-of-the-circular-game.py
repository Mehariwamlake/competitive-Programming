class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return self.helper(n, k) + 1
        
    def helper(self, n: int, k: int) -> int:
        if (n==1):
            return 0
        preWinner = self.helper(n-1, k)
        Winner = (preWinner + k) % n
        return Winner
