'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example
1:

Input: strs = ["flower", "flow", "flight"]
Output: "fl"
Example
2:

Input: strs = ["dog", "racecar", "car"]
Output: ""
Explanation: There is no
common
prefix
among
the
input
strings.

Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i]
consists
of
only
lower - case
English
letters.'''

class Solution:
    def longestCommonPrefix(self, strs):
        s = ''
        i = 0
        x = True
        if len(strs) > 1:
            while x == True:
                for j in range(len(strs)-1):
                    try:
                        if strs[j][i] != strs[j+1][i]:
                            x = False
                            break
                    except:
                        x = False
                        break
                if x == True:
                    try:
                        s = s + strs[0][i]
                    except:
                        x = False
                i+=1
        elif len(strs) == 1:
            s = strs[0]
        return(s)

result = Solution()
x = ["flower","flow","flight"]
print(result.longestCommonPrefix(x))