class Solution:
    def largestOddNumber(self, num: str) -> str:
        j=len(num)-1
        while(j>=0):
            if int(num[j]) %2 !=0:
                return num[:j+1]
            j=j-1
        return ""

        