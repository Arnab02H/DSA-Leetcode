class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ## At first remove all the special charecter and space , also convert into lower charecter
        # new=("".join(char for char in s if char.isalnum())).lower()
        # return new==new[::-1]
        lst=[]
        for i in range(len(s)):
            if s[i].isalnum():
                lst.append(s[i].lower())
        newStr="".join(lst)
        return newStr==newStr[::-1]