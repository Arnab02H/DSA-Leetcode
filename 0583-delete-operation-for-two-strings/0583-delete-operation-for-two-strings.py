class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n,m=len(word1),len(word2)
        memo=[[-1]*(m+1) for i in range(n+1)]
        def helper(i,j):
            if i==0 or j==0:
                return 0
            if memo[i][j]!=-1:
                return memo[i][j]
            if word1[i-1]==word2[j-1]:
                memo[i][j]=1+helper(i-1,j-1)
            else:
                memo[i][j]=max(helper(i-1,j),helper(i,j-1))
            return memo[i][j]
        a=helper(n,m)
        return (n-a)+(m-a)
        
        