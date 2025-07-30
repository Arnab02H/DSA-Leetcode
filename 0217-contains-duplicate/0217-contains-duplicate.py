from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp=defaultdict()
        for i in nums:
            if i not in temp:
                temp[i]=1
            else:
                return True 
        return False
        