'''Given a string s containing just the characters '(', ')',
'{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true'''

class Solution:
    def isValid(self, s):

        braces = {')': '(', '}': '{', ']': '['}
        stack = []

        for i, c in enumerate(s, start=1):
            if c in braces.values():
                stack.append((c, i))
            if c in braces and (not stack or braces[c] != stack.pop()[0]):
                return False
        return False if stack else True

result = Solution()

s = "{[]}"
print(result.isValid(s))