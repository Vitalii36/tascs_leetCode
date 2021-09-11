"""Given a string containing just the characters '(' and ')', find the length of
the longest valid (well-formed) parentheses substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0"""


def count(s):
    s = s.replace("()", "*")
    for i in range(1, len(s)):
        s = s.replace(f"(" + i * "*" + ")", (i + 1) * "*")
    s = s.replace(")", "(")
    s = s.split("(")
    return max(len(p) for p in s) * 2

class Solution:
    def longestValidParentheses(self, s):
        return count(s)

result = Solution()

s = "()(()"
# s = ""
# s = "(()"
# s = ")()())"
# s = "()()"
print(result.longestValidParentheses(s))