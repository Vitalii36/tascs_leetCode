'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is
a bijection between a letter in pattern and a non-empty word in s.


Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", s = "dog dog dog dog"
Output: false
'''


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        phrases, d = s.split(' '), {}
        if len(pattern) != len(phrases):
            return False
        for i in range(len(pattern)):
            if not d.get(pattern[i]):
                if phrases[i] in d.values():
                    return False
                d[pattern[i]] = phrases[i]
            elif d[pattern[i]] != phrases[i]:
                return False
        return True
