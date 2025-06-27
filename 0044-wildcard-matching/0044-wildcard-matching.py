class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        memo = [[None] * (m + 1) for _ in range(n + 1)]

        def helper(i, j):
            if i < 0 and j < 0:
                return True
            if i >= 0 and j < 0:
                return False
            if i < 0 and j >= 0:
                for k in range(j + 1):
                    if p[k] != '*':
                        return False
                return True
            if memo[i][j] is not None:
                return memo[i][j]

            if p[j] == s[i] or p[j] == '?':
                memo[i][j] = helper(i - 1, j - 1)
            elif p[j] == '*':
                memo[i][j] = helper(i - 1, j) or helper(i, j - 1)
            else:
                memo[i][j] = False

            return memo[i][j]

        return helper(n - 1, m - 1)
