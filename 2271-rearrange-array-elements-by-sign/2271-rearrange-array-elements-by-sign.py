class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ## separate positive and negative number 
        pos,neg=[],[]
        for i in range(len(nums)):
            if nums[i]<0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        ans=[]
        for i in range(max(len(pos),len(neg))):
            if i<=len(pos):
                ans.append(pos[i])
            if i<=len(neg):
                ans.append(neg[i])
        for i in range(len(nums)):
            nums[i]=ans[i]
        return nums

        
        