from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 == 1:
            return False 
        
        target = total // 2
        n = len(nums)
        
        # Create a DP table initialized with None
        temp = [[-1 for _ in range(target + 1)] for _ in range(n + 1)]
        
        return self.subsetSum(nums, target, temp)

    def subsetSum(self, A: List[int], target: int, temp: List[List[bool]]) -> bool:
        n=len(A)
        if target == 0:
            return True
        if n == 0:
            return False
        
        if temp[n][target] !=-1:
            return temp[n][target]

        if A[n - 1] <= target:
            temp[n][target] = self.subsetSum(A[:n-1], target - A[n - 1], temp) or self.subsetSum(A[:n-1],target, temp)
        else:
            temp[n][target] = self.subsetSum(A[:n-1], target, temp)
        
        return temp[n][target]
