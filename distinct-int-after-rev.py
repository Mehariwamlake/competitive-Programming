class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = set(nums)

        for n in nums:
            strN =str(n)
            strR = strN[::-1]
            s.add(int(strR))
            
        return len(s)
