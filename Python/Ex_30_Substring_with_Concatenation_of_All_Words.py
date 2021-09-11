"""You are given a string s and an array of strings words of the same length.
Return all starting indices of substring(s) in s that is a concatenation of
each word in words exactly once, in any order, and without any intervening
characters.
You can return the answer in any order.

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar"
respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]"""


class Solution:
    def findSubstring(self, s, words):
        w_len = len(words[0])
        tot_len = w_len * len(words)
        rtn = []
        words.sort()

        for i in range(0, len(s) - tot_len + 1):

            temp = s[i:i + tot_len]
            temp_list = []

            for j in range(0, len(temp), w_len):
                temp_list.append(temp[j:j + w_len])

            temp_list.sort()

            if (temp_list == words):
                rtn.append(i)

        return rtn

result = Solution()

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]
# s = "barfoofoobarthefoobarman"
# words = ["bar","foo","the"]
print(result.findSubstring(s, words))