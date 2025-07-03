class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        summ=0
        for i in nums:
            summ+=i
            maxi=max(summ,maxi)
            if summ<0:
                summ=0
        return maxi
    
        