from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d=defaultdict(int)
        res=0
        for num in nums:
            if not d[num]:
                d[num]=d[num-1]+d[num+1]+1
                d[num-d[num-1]]=d[num]
                d[num+d[num+1]]=d[num]
                res=max(res,d[num])
        return res