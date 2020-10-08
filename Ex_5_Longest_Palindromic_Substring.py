'''Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
'''

class Solution:
    def longestPalindrome(self, s):
        palin = [[False for i in range(len(s))] for j in range(len(s))]

        for i in range(len(s)):
            # string of len 1 is palindrome
            palin[i][i] = True
        start = 0
        length = 1
        for i in range(len(s) - 1):
            # s[i] and s[i+1] is same its palindromee.g. aa, bb... etc
            if s[i] == s[i + 1]:
                palin[i][i + 1] = True

                start = i
                length = 2
        # now check for string len more than 2
        for k in range(2, len(s)):
            for i in range(len(s) - k):
                j = i + k

                if palin[i + 1][j - 1] and s[i] == s[j]:
                    palin[i][j] = True
                    # print("palin{}{}..{}".format(i,j,s[i:j+1]))
                    if k + 1 > length:
                        start = i
                        length = k + 1
        return s[start:start + length]

result = Solution()
s = "a"
print(result.longestPalindrome(s))