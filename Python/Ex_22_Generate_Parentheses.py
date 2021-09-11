'''Given n pairs of parentheses, write a function to generate
all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''

class Solution:
    def generateParenthesis(self, n):
        d = {0: [""]}
        for i in range(2, 2 * n + 1, 2):
            strs = []
            for j in range(0, i, 2):
                part1size = j
                part2size = i - j - 2
                for part1 in d[part1size]:
                    for part2 in d[part2size]:
                        strs.append('(' + part1 + ')' + part2)
            d[i] = strs
        return d[2 * n]



result = Solution()

n = 3
print(result.generateParenthesis(n))