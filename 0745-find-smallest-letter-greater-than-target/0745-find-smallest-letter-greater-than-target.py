class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n=len(letters)
        low,high=0,n-1
        while low<=high:
            mid=(low+high)//2
            if letters[mid]<=target:
                low=mid+1
            else:
                high=mid-1
        return letters[low % n]
        