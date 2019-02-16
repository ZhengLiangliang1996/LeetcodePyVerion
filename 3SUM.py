#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 22:22:32 2019

@author: liangliang
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        if len(nums) < 3:
            return res
        
        # pair wise sum
        for i in range(len(nums)):
            # -a - b = c
            # -a 
            target = 0 - nums[i]
            hashmap = {}
            for j in range(i + 1, len(nums)):
                if (target - nums[j]) in hashmap:
                    res_sub = [nums[i], target - nums[j], nums[j]]
                    if res_sub not in res:
                        res.append(res_sub)
                else:
                     hashmap[nums[j]] = j
        return res
                    
                
                

def main():
    S = Solution()
    a = S.threeSum([-1, 0, 1, 2, -1, 4])
    print(a)
    
if __name__ == '__main__':
    main()
        