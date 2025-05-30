class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total_sum=int((n*(n+1))/2)
        summ=0
        for i in range(n):
            summ+=nums[i]
        return total_sum-summ
        