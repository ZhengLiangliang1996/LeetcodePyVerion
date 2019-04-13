#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 10:04:12 2019

@author: liangliang
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # recursive way 
        if root == None:
            return 0
        
        left_dep = self.maxDepth(root.left)
        right_dep = self.maxDepth(root.right)
        
        return max(left_dep, right_dep) + 1