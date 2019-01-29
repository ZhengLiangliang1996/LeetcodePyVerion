# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 22:29:18 2019

@author: zhengstars
"""

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #https://www.youtube.com/watch?v=5o-kdjv7FD0
        if n == 0 or n == 1: 
            return 1
        a = [0 for i in range(n+1)] 
        #初始化
        a[0] = 1
        a[1] = 1
        for j in range(2,n+1):
            a[j] = a[j - 1] + a[j - 2]
        return a[n]
    
a = Solution()
print(a.climbStairs(3))
            