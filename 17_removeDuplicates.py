#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 23:19:34 2019

@author: liangliang
"""
import numpy as np

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        Given nums = [0,0,1,1,1,2,2,3,3,4],

        Your function should return length = 5, with 
        the first five elements of nums being modified to
         0, 1, 2, 3, and 4 respectively.
        '''
        if len(nums)==0:
            return 0
        cur = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[cur]:
                cur += 1
                nums[cur] = nums[i]
        return cur+1

def main():    
    S = Solution()
    nums = [1,1,2]
    a = S.removeDuplicates(nums)
    print(a)
    

if __name__ == '__main__':
    main()