class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first=prices[0]
        maxi=0
        for i in range(1,len(prices)):
            profit=prices[i]-first
            maxi=max(profit,maxi)
            first=min(first,prices[i])
        return maxi
            