"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
"""
from collections import Counter


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        board_dic = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                board_dic[board[i][j]] += 1

        word_dic = Counter(word)
        for c in word_dic:
            if c not in board_dic or board_dic[c] < word_dic[c]:
                return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, 0, board, word):
                        return True

        return False

    def dfs(self, i, j, k, board, word):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or \
        k >= len(word) or word[k] != board[i][j]:
            return False

        if k == len(word) - 1:
            return True

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x, y in directions:
            tmp = board[i][j]
            board[i][j] = -1

            if self.dfs(i + x, j + y, k + 1, board, word):
                return True

            board[i][j] = tmp