class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi,index,area=0,0,0
        x=0
        i,j=0,len(height)-1
        while i<j:
            if height[i]<=height[j]:
                x=height[i]
                index=i
            else:
                x=height[j]
                index=j
            maxi=max(maxi,x*(j-i))
            if index==i:
                i+=1
            else:
                j-=1
        return maxi

        