class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)]
        ## This loop will do that in count dictionary it store all number frequency
        for num in nums:
            count[num]=count.get(num,0)+1
        arr=[]
        for n,c in count.items():
            arr.append([c,n])
        arr.sort()
        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res
        