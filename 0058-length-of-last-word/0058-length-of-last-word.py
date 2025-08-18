class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        newStr=s[::-1].strip()
        count=0
        
        for i in range(len(newStr)):
            if newStr[i]!=" ":
                count+=1
            else:
                break
        return count
            
        