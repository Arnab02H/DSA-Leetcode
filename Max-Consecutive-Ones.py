class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count,maxi=0,0
        n=len(nums)
        for i in range(n):
            if nums[i]==1:
                count+=1
                if count>maxi:
                    maxi=count
            else:
                count=0
        return maxi
        