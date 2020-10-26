'''Given a string containing digits from 2-9 inclusive, return all possible
letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is
given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]'''

class Solution:
    def letterCombinations(self, digits):


        alphabet = {2:['a', 'b', 'c'], 3:['d', 'e', 'f'], 4:['g', 'h', 'i'], 5:['j', 'k', 'l'],
                    6:['m', 'n', 'o'],7:['p', 'q', 'r', 's'], 8:['t', 'u', 'v'], 9:['w', 'x', 'y', 'z']}
        try:
            if len(digits) == 1:
                return (alphabet[int(digits)])
            else:
                ls = alphabet[int(digits[len(digits) - 1])]
                digits = digits[:len(digits) - 1]
                for i in range(len(digits) - 1, -1, -1):
                    ls_prom = []
                    for j in alphabet[int(digits[i])]:
                        for k in ls:
                            ls_prom.append(j + k)
                    ls = ls_prom.copy()
                return (ls)
        except:
            return([])



result = Solution()
digits = "2"
print(result.letterCombinations(digits))