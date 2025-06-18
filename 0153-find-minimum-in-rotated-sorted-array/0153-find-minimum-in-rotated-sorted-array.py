class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,high=0,len(nums)-1
        mini=float('inf')
        while(low<=high):
            mid=(low+high)//2
            if nums[low]<=nums[mid]: ## that means left half is sorted 
                mini=min(nums[low],mini)
                low=mid+1
            else: ## right half is sorted 
                mini=min(mini,nums[mid])
                high=mid-1
        return mini
                
            