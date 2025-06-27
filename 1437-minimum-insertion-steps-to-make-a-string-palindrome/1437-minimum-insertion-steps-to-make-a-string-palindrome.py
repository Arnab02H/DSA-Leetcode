class Solution:
    def minInsertions(self, s: str) -> int:
        p=s[::-1]
        n,m=len(s),len(p)
        memo=[[-1]*(m+1) for i in range(n+1)]
        def helper(i,j):
            if i==0 or j==0:
                return 0
            if memo[i][j]!=-1:
                return memo[i][j]
            if s[i-1]==p[j-1]:
                memo[i][j]=1+helper(i-1,j-1)
            else:
                memo[i][j]=max(helper(i-1,j),helper(i,j-1))
            return memo[i][j]
        return len(s)-helper(n,m)
        
        