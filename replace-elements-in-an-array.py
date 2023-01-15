class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        look = {}
        for i, x in enumerate(nums):
            look[x]= i

        for x, y in operations:
            index = look[x]

            nums[index] = y
            look[y] = index
            del look[x]
        return nums