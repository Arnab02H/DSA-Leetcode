
class Solution:
    def word2dict(self,word):
        d={}
        for letter in word:
            d[letter]=d.get(letter,0)+1  ## if letter not present in dictionary it will 0+1 other if present then it is value+1
        return d
    def isAnagram(self, s: str, t: str) -> bool:
        return self.word2dict(s)==self.word2dict(t)

        