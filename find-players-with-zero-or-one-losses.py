class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[] for i in range(2)]
        lossesCount = Counter()

        for winner, loser in matches:
            if winner not in lossesCount:
                lossesCount[winner] = 0
            lossesCount[loser] +=1

        for player, numLosses in lossesCount.items():
            if numLosses < 2:
                ans[numLosses].append(player)

        return [sorted(ans[0]), sorted(ans[1])]