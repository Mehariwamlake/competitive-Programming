class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = collections.deque(word1)
        w2 = collections.deque(word2)
        res = []
        while len(w1) > 0 and len(w2) > 0:
            res.append (w1.popleft())
            res.append (w2.popleft())

        while len(w1) > 0:
            res.append (w1.popleft())
        while len(w2) > 0:
            res.append (w2.popleft())

        return ''.join(res)