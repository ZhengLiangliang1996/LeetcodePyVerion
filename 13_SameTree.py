#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:32:43 2019

@author: liangliang
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None: return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False


def main():
    T1 = TreeNode(1)
    #T1.left = TreeNode(2)
    #T1.right = TreeNode(3)
  
    T2 = None
    #T2.left = TreeNode(2)
    #T2.right = TreeNode(3)
  
    S = Solution()
    a = S.isSameTree(T1, T2)
    print(a)
    

if __name__ == '__main__':
    main()
        
        