class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        col=len(grid[0])
        negativeCount=0
        for i in range(rows):
            for j in range(col):
                if grid[i][j]<0:
                    negativeCount+=1
        return negativeCount 