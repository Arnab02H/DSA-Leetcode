class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        low,high=0,(row*col)-1
        while(low<=high):
            mid=(low+high)//2
            mid_val= matrix[mid//col][mid%col]
            if mid_val==target:
                return True
            elif mid_val>target:
                high=mid-1
            else:
                low=mid+1
        return False

        