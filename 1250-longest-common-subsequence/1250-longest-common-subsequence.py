class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        Method-1: Tabulation Approach
        n,m=len(text1),len(text2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    a=dp[i][j-1]
                    b=dp[i-1][j]
                    dp[i][j]=max(a,b)
        return dp[n][m]'''
        ### Method-2: Memoization 
        n,m=len(text1),len(text2)
        memo=[[-1]*(m+1) for i in range(n+1)]
        def helper(i,j):
            if i==0 or j==0:
                return 0
            if memo[i][j]!=-1:
                return memo[i][j]
            if text1[i-1]==text2[j-1]:
                memo[i][j]=1+helper(i-1,j-1)
            else:
                memo[i][j]=max(helper(i-1,j),helper(i,j-1))
            return memo[i][j]
        return helper(n,m)