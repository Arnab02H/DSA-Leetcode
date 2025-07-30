class Solution:
    def isPalindrome(self, s: str) -> bool:
        ## At first remove all the special charecter and space , also convert into lower charecter
        new=("".join(char for char in s if char.isalnum())).lower()
        return new==new[::-1]