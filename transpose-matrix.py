class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        Rows, Cols = len(matrix), len(matrix[0])
        output = [[0]*Rows for i in range (Cols)]

        for r in range(Rows):
            for c in range(Cols):
                output[c][r] = matrix[r][c]
        return output