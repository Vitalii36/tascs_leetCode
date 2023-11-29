"""
Given a string s, partition the string into one or more substrings such that the
characters in each substring are unique. That is, no letter appears in a single
substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.



Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
Example 2:

Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").


Constraints:

1 <= s.length <= 105
s consists of only English lowercase letters.
"""


class Solution:
    def partitionString(self, s: str) -> int:
        res, par, s2 = [], '', s
        while s:
            if s[0] not in par:
                par = par + s[0]
            else:
                res.append(par)
                par = s[0]
            s = s[1:]
        if par:
            res.append(par)

        res2, par2 = [], ''
        while s2:
            if s2[-1] not in par2:
                par2 = par2 + s2[-1]
            else:
                res2.append(par2)
                par2 = s2[-1]
            s2 = s2[:-1]
        if par:
            res2.append(par2)

        return len(res) if len(res) < len(res2) else len(res2)
