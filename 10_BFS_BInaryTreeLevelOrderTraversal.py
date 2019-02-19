#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 21:35:45 2019

@author: liangliang
"""

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        Use Queue for BFS
        """
        if root == None: 
            return []
        res = [] # for storing result
        q = [root] # each result for every breath
        while len(q) != 0:           
            res.append([i.val for i in q])
            queue = [] # result in a breath
            for node in q:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            q = queue
        res.reverse()
        return res
                

def main():
    T1 = TreeNode(3)
    T1.left = TreeNode(9)
    T1.right = TreeNode(20)
    T1.right.left = TreeNode(15)
    T1.right.right = TreeNode(7)
    
    S = Solution()
    a = S.levelOrder(T1)
    print(a)
    

if __name__ == '__main__':
    main()