class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        ''' 
        RECURSIVE CODE:
        if n==0:
                return 0
            if n==1:
                return nums[0]
            if n==2:
                return max(nums[0],nums[1])
            ans=0
            summ=max(nums[0]+self.rob(nums[2:]),self.rob(nums[1:]))
            if summ>ans:
                ans=summ
            return ans'''

        ### Memoization Version
        dp = [-1] * n

        def help(i):
            if i < 0:
                return 0
            if dp[i] != -1:
                return dp[i]
            if i == 0:
                dp[i] = nums[0]
            else:
                dp[i] = max(nums[i] + help(i - 2), help(i - 1))
            return dp[i]

        return help(n - 1)