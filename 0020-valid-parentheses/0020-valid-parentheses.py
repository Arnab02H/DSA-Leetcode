class Solution:
    def isValid(self, s: str) -> bool:
        parent = ['(', '{', '[']
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] in parent:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if (s[i] == ')' and stack[-1] == '(') or \
                   (s[i] == '}' and stack[-1] == '{') or \
                   (s[i] == ']' and stack[-1] == '['):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
