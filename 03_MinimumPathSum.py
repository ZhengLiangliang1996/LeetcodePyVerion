# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 23:07:50 2019

@author: zhengstars
"""

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # refer to https://www.youtube.com/watch?v=dC8vqaZ-7Ow
        # O(m * n)
        # space O(1)
        m = len(grid)
        n = len(grid[0])
        
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
            
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
            
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])
                    
        return grid[m-1][n-1]
    
l = [[1,3,1],[1,5,1],[4,2,1]]
a = Solution()
print(a.minPathSum(l))