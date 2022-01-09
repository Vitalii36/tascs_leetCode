'''
Given a string s, check if it can be constructed by
taking a substring of it and appending multiple copies
of the substring together.



Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or
the substring "abcabc" twice.


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
'''


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = int(round(len(s) / 2, 0))
        for i in range(2, l + 1):
            if len(s) == (len(s[:i]) * s.count(s[:i])):
                return True
        if len(list(set(s))) == 1 and len(s) != 1:
            return True
        return False


result = Solution()
# s = "abcabcabcabc"
s = "aba"
# s = "adadad"
# s = "abc"

print(result.repeatedSubstringPattern(s))