#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 09:49:13 2019

@author: liangliang
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return None
        
        pre_node = head
        
        current = pre_node.next

        while current:
            # if same, then jump pointer to the next node
            if current.val == pre_node.val:
                pre_node.next = current.next
            # else only move prenode to the current node
            else:
                pre_node = current
            # each round, get the curr to the next node
            current = current.next
        
        return head