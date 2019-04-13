#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:58:12 2019

@author: liangliang
"""

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        
        
        if head.next == None:
            return False
        # using set to distinguish
        s = set()
        temp = head
        
        while temp:
            if temp in s:
                return True
            
            s.add(temp)
            
            # get to the next node
            temp = temp.next
    
        return False