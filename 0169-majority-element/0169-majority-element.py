class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        ans=None
        for i in range(len(nums)):
            if cnt==0:
                cnt=1
                ans=nums[i]
            elif nums[i]==ans:
                cnt+=1
            else:
                cnt-=1
        final_count=0
        for i in range(len(nums)):
            if ans==nums[i]:
                final_count+=1
                if final_count>(len(nums)/2):
                    return ans 
        

        