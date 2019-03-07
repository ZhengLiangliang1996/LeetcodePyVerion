p#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:42:39 2019

@author: liangliang
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]
        
def main():
    S = Solution()
    a = S.addBinary('11','1')
    print(a)

if __name__ == '__main__':
    main()
        
    