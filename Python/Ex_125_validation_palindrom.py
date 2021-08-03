'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''


class Solution:
    def isPalindrome(self, s):
        import re
        s = s.lower()
        p = ''.join(re.findall('[0-9a-z]', s))
        print(p, p[::-1])
        if p == p[::-1]:
            return True
        return False


result = Solution()
# string = 'A man, a plan, a canal: Panama'
string = "0P"
print(result.isPalindrome(string))
