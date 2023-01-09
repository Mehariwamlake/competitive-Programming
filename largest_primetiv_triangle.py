class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        for i in range (n-3, -1, -1):
            a, b, c = (nums[i], nums[i + 1], nums[i + 2])
            if a + b > c:
                return a + b + c
        return 0