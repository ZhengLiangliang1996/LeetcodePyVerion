#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 22:08:36 2019

@author: liangliang
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        s = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[s] = nums[i]
                s = s + 1
        for i in range(len(nums)):
            print(nums[i])
        return s


def main():
    S = Solution()
    a = S.removeElement([1,2,2,3,4],2)
    print(a)
    
if __name__ == '__main__':
    main()
        