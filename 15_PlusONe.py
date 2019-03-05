#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:26:23 2019

@author: liangliang
"""
from functools import reduce

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # final '' is the initializer
        # reduce(function, iterable[, initializer])
        s = reduce(lambda x,y: x+str(y), digits, '')
        num = int(s)
        print(num)
        return [int(d) for d in str(num+1)]

def main():
    S = Solution()
    a = S.plusOne([1,2,3])
    print(a)

if __name__ == '__main__':
    main()
        