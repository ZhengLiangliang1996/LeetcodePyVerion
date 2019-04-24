#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 22:45:05 2019

@author: liangliang
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n = len(board)
        m = len(board[0])
        if n == 0:
            return 0
        
        def dfs(x, y, n, m, board, word):
            if len(word) == 0:
                return True
            if x < 0 or y < 0 or x >= n or y >= m or word[0] != board[x][y]:
                return False
            # save the board to temp 
            temp = board
            board[x][y] = '!'
            # four different direction
            res = dfs(x + 1, y, n, m, board, word[1:]) or dfs(x, y + 1, n, m, board, word[1:]) or dfs(x - 1, y, n, m, board, word[1:]) or dfs(x, y - 1, n, m, board, word[1:])
            # take back the original one for backtracking
            board = temp
            return res
        
        for i in range(n):
             for j in range(m):
                if dfs(i, j, n, m, board, word) == True:
                    return True
        return False
            
def main():
    S = Solution()
    board =[
     ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
]
    word = "ABCB"
    a = S.exist(board, word)
    print(a)
    
if __name__ == "__main__":
    main()
    