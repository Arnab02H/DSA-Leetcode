class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i,j=0,len(nums)-1
        ans=[0]*len(nums)
        pos=n-1
        while i <=j:
            ls=nums[i]**2
            rs=nums[j]**2
            if ls>rs:
                ans[pos]=ls
                i+=1
            else:
                ans[pos]=rs
                j-=1
            pos-=1
        return ans
        