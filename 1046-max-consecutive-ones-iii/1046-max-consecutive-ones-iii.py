class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_len = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # If zero_count > k, shrink window from the left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Update the max length of window
            max_len = max(max_len, right - left + 1)

        return max_len
        