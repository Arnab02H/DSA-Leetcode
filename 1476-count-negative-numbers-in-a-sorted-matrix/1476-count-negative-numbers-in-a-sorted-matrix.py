class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ## Noob Approach
        # rows=len(grid)
        # col=len(grid[0])
        # negativeCount=0
        # for i in range(rows):
        #     for j in range(col):
        #         if grid[i][j]<0:
        #             negativeCount+=1
        # return negativeCount 

        ### Optimal Approach 
        row,cols=len(grid),len(grid[0])
        negative=0
        i,j=row-1,0
        while i>=0 and j<cols:
            if grid[i][j]<0:
                negative+=cols-j
                i-=1
            else:
                j+=1
        return negative