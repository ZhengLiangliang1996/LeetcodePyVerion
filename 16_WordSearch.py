#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 22:58:48 2019

@author: liangliang
"""
import numpy as np

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # get 1, then dfs, all the connected 1, mark them as 0
        n = len(board)
        m = len(board[0])
        if n == 0:
            return 0
        
        for i in range(n):
            for j in range(m):
                if self.dfs(board, i, j, n, m, word):
                    return True
        return False
        
    def dfs(self, board, x, y, n, m, word):
        if len(word) == 0:
            return True
        
        if x < 0 or y < 0 or x >= n or y >= m or word[0] != board[x][y]: 
            return False
        
        temp = board[x][y]
        
        board[x][y] = "#"  # avoid visit agian 

        res = self.dfs(board, x + 1, y, n, m, word[1:]) or self.dfs(board, x - 1, y, n, m, word[1:]) or self.dfs(board, x, y + 1, n, m, word[1:]) or self.dfs(board, x, y - 1, n, m, word[1:]) 
        
        board[x][y] = temp
        return res
        
def main():
    S = Solution()
    board = [
                ['A','B','C','E'],
                ['S','F','C','S'],
                ['A','D','E','E']
            ]
    a = S.exist(board, 'ABCED')
    print(a)

if __name__ == '__main__':
    main()
        
        