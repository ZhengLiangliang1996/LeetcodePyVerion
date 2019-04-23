#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 08:47:08 2019

@author: liangliang
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # has something to do with rotate: using Modulo Operation
        k %= len(nums)
        for i in range(len(nums) - k):
            temp = nums.pop(0)
            nums.append(temp)
        
        
def main():
    S = Solution()
    nums = [1,2,3,4,5,6,7]
    S.rotate(nums, 3)
    print(nums)
    
if __name__ == "__main__":
    main()