'''Given a string s, find
the length of the longest
substring without repeating
characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The
answer is "abc",
with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The
answer is "b",
with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The
answer is "wke",
with the length of 3.
Notice that the answer
must  be a substring, "pwke" is a
subsequence and not a
substring.
Example
4:

Input: s = ""
Output: 0'''

class Solution:
    def lengthOfLongestSubstring(self, s):

        if len(s) == 0:
            return 0

        l = []
        max = 0
        for i in range(len(s)):
            if s[i] not in l:
                l.append(s[i])
            else:

                if len(l) > max:
                    max = len(l)
                l = l[l.index(s[i]) + 1:]
                l.append(s[i])
        return max if max > len(l) else len(l)

result = Solution()
s = "aabaab!bb"
print(result.lengthOfLongestSubstring(s))

