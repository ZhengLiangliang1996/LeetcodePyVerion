#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 21:23:16 2019

@author: liangliang
"""
import math 

class Solution(object):
    def lengthOfLongestSubstring(self, s):
            """
            :type s: str
            :rtype: int
            https://www.youtube.com/watch?v=hw0zHamgaks
            """
            if(s == None or len(s) == 0):
                return 0
            # HashMap
            map1 = {}
            res = 0
            j = 0 # abc j = 0 when i goes to abca there is repetition then, j should be 1 instead of 0
            for i in range(len(s)):
               # whether s[i] in map
                if (s[i] in map1):
                    j = max(j, map1[s[i]] + 1)
                map1[s[i]] = i
                res = max(res, i - j + 1)
            return res

S = Solution()
print(S.lengthOfLongestSubstring("abcabcacbbbb"))

        
        