class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findFirst():
            low,high=0,len(nums)-1
            first=-1
            
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
           
                    first=mid
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return first
        def findSecond():
            low,high=0,len(nums)-1
            second=-1
            while low<=high:
                mid=(low+high)//2

                if nums[mid]==target:
                    second=mid
                    low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return second
        first=findFirst()
        last=findSecond()
        return [first,last]

        