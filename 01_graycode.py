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
        # 公式 G（i） = i ^ (i / 2)
        # 
        y = []
        for i in range(2 << n):
            y.append(i ^ i >> 1)
        return y