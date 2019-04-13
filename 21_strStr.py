#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 09:22:17 2019

@author: liangliang
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        
        if needle in haystack:
            # start from the first matched symbol
            for i in range(haystack.index(needle[0]), len(haystack) - len(needle) + 1):
                if haystack[i:i+len(needle)] == needle:
                    return i
        else:
            return -1
        
        