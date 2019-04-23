#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:45:00 2019

@author: liangliang
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 减去之后存在于字典当中
        dictionary = {}
        for i, number in enumerate(numbers):
            if (target - number) in dictionary:
                return [dictionary[target - number] + 1, i + 1]
            dictionary[number] = i
        # 其实还可以用二分法 因为有排序

def main():
    S = Solution()
    a = S.twoSum([2,7,11,5], 9)
    print(a)
    
if __name__ == "__main__":
    main()