class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        n,m=len(s),len(t)
        dp=[[None]*(m+1) for i in range(n+1)]
        def helper(i,j):
            if j<=0:
                return 1 
            if i<=0:
                return 0
            if dp[i][j]!=None:
                return dp[i][j]
            if s[i-1]==t[j-1]:
                dp[i][j]=helper(i-1,j-1)+helper(i-1,j)
            else:
                dp[i][j]=helper(i-1,j)
            return dp[i][j]
        return helper(n,m)
        