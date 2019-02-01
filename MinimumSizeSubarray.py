# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 20:20:48 2019

@author: zhengstars
"""


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # SLIDING WINDOW可以解答
        res = 10**100
        sum1 = 0
        left = 0
        for i in range(len(nums)):
            sum1 += nums[i]
            while left <= i and sum1 >= s:
                res = min(res, i - left + 1)
                sum1 -= nums[left]
                left += 1
        if res == 10**100:
            res =  0 
        return res
    
s = Solution()
print(s.minSubArrayLen(7, [1,2,3,4,5,6]))
