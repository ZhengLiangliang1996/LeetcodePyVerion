#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 22:56:00 2019

@author: liangliang
"""

import math 

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.floor(math.sqrt(x)))
    
def main():
    S = Solution()
    a = S.mySqrt(8)
    print(a)

if __name__ == '__main__':
    main()
        
        