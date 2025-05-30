class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_of_index={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in nums_of_index:
                return [nums_of_index[complement],i]
            nums_of_index[num]=i
        return []