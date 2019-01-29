# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 22:19:09 2019

@author: zhengstars
"""
import numpy as np
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        return nums1.sort()
    
s = Solution()
print(s.merge([1,2,3],3,[1,2,3],2))