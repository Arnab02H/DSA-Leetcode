import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high=1,max(piles)
        ans=float('inf')
        while low<=high:
            mid=(low+high)//2
            totalTime=self.calculateTime(piles,mid)
            if totalTime<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans 
    def calculateTime(self,arr,i):
        totalTime=0
        for j in range(len(arr)):
            totalTime+=math.ceil(arr[j]/i)
        return totalTime

        