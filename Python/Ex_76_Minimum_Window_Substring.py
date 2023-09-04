"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there
is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = {}
        for char in t:
            if char in t_map:
                t_map[char] += 1
            else:
                t_map[char] = 1

        left = 0
        right = 0
        min_len = float('inf')
        min_start = 0
        char_needed = len(t_map)
        window_map = {}

        while right < len(s):
            char = s[right]
            if char in t_map:
                if char in window_map:
                    window_map[char] += 1
                else:
                    window_map[char] = 1

                if window_map[char] == t_map[char]:
                    char_needed -= 1

            while char_needed == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                char = s[left]
                if char in t_map:
                    window_map[char] -= 1
                    if window_map[char] < t_map[char]:
                        char_needed += 1
                left += 1

            right += 1

        if min_len == float('inf'):
            return ""
        else:
            return s[min_start:min_start + min_len]
