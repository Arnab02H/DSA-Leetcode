class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el=None
        cnt=0
        for i in range(len(nums)):
            if cnt==0:
                cnt=1
                el=nums[i]
            elif el==nums[i]:
                cnt+=1
            else:
                cnt-=1
        ans=0
        for i in range(len(nums)):
            if el==nums[i]:
                ans+=1
            if ans>(len(nums)//2):
                return el

