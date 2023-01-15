class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        foodDict = {}
        for  food in deliciousness:
            foodDict[food] = foodDict.get(food)