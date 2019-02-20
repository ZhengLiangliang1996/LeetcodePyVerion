#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 19:26:43 2019

@author: liangliang
"""

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
     
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        q = [root]
        res = []
        count = 2
        while len(q) != 0:
            res.append([i.val for i in q])
            queue = []
            for i in q:
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
            q = queue
        for i in range(len(res)):
            if i%2 == 1:
                res[i].reverse()
        return res
         
def main():
    T1 = TreeNode(3)
    T1.left = TreeNode(9)
    T1.right = TreeNode(20)
    T1.right.left = TreeNode(15)
    T1.right.right = TreeNode(7)
    
    S = Solution()
    a = S.zigzagLevelOrder(T1)
    print(a)
    

if __name__ == '__main__':
    main()