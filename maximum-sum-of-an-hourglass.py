class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        DIR = [
            (0,0), # d
            (-1, -1), #a
            (-1, 0),
            (-1, 1),
            (1, -1),
            (1, 0),
            (1, 1)
        ]

        max_sum = 0
        for i in range(1, n -1):
            for j in range(1, m - 1):
                cur_sum = 0
                for di, dj in DIR:
                    cur_sum += grid[i + di][j + dj]
                max_sum = max(max_sum, cur_sum)
        return max_sum
        