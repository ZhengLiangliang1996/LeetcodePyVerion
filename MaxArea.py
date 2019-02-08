#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 17:07:57 2019

@author: liangliang
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #https://www.youtube.com/watch?v=wLo0xIRDjQc
        res = 0
        l = 0
        r = len(height) - 1
        while(l < r):
            # choose the lowest height (mu tong yuan li)
            res = max(res, min(height[l], height[r]) * (r - l))
            # moving l or r
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
                
        return res

S = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(S.maxArea(height))


                