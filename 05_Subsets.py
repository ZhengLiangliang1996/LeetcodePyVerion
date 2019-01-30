# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 20:36:59 2019

@author: zhengstars
"""

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # https://www.youtube.com/watch?v=Az3PfUep7gk
        # 2的n次方的子集
        # 将这个问题分解成二元问题 最开始是{} 然后问 加一个元素 否 {}  是 {1} 然后可以构成树
        self.res = []
        def dfs(nums, temp, i):
            self.res.append(temp[:]) #潜复制得到temp 不然会改变temp的值
            for i in range(i, len(nums)):
                temp.append(nums[i])
                dfs(nums, temp, i + 1)
                temp.pop()
        dfs(nums, [], 0)
        return self.res
            