class Solution:
    def climbStairs(self, n: int) -> int:
        memo=[None]*(n+1)
        def helper(n):
            if n<=1:
                return 1
            if memo[n] !=None:
                return memo[n]
            memo[n]=helper(n-1)+helper(n-2)
            return memo[n]
        return helper(n)