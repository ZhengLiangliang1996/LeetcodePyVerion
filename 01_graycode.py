# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:53:40 2019

@author: zhengstars
"""
import math

class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        y = []
        if(n == 0):
            return y.append()
        a = int(math.pow(2, n))
        for i in range(a):
            y.append(i)
        return y
    
a = Solution()
a.grayCode(4)