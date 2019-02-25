#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:22:18 2019

@author: liangliang
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # get 1, then dfs, all the connected 1, mark them as 0
        n = len(grid)
        m = len(grid[0])
        if n == 0:
            return 0
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res += 1
                    self.dfs(grid, i, j, n, m)
        return res
    
    def dfs(self, grid, x, y, n, m):
        if x < 0 or y < 0 or x >= n or y >= m or grid[x][y] == 0:
            return 
        grid[x][y] = 0
        self.dfs(grid, x + 1, y, n, m)
        self.dfs(grid, x - 1, y, n, m)
        self.dfs(grid, x, y + 1, n, m)
        self.dfs(grid, x, y - 1, n, m)
        
