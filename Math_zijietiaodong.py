#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:03:16 2019

@author: liangliang
"""
import math

class Solution(object):
    def LeastCoin(self, n):
        """
        :type digits: str
        :rtype: List[str]
        """
        rec = 1024 - n
        num64 = math.floor(rec / 64)
        rec = rec - 64*num64
        num16 = math.floor(rec / 16)
        rec = rec - 16*num16
        num4 = math.floor(rec / 4)
        rec = rec - 4*num4
        num1 = math.floor(rec / 1)
        rec = rec - 1*num1

        return num64+num16+num4+num1
        
        
                
def main():
    S = Solution()
    a = S.LeastCoin(1000)
    print(a)
    
if __name__ == "__main__":
    main()
