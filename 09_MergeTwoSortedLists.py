#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 22:12:56 2019

@author: liangliang
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        i = 0
        #head = ListNode()
        while(l1 and l2):
            if i == 0:
                head = L3 = ListNode(0)
            if l1.val < l2.val:
                L3.next = l1
                l1 = l1.next
            else: 
                L3.next = l2
                l2 = l2.next
            
            L3 = L3.next
            i +=1
        L3.next = l1 or l2 # that is l1 and l2 then there would be one left
        return head.next
            
        
def main():
    L = ListNode(1)
    L.next = ListNode(2)
    L.next.next = ListNode(4)
    
    L1 = ListNode(1)
    L1.next = ListNode(3)
    L1.next.next = ListNode(4)
    
    S = Solution()
    L3 = S.mergeTwoLists(L, L1)
    print(L3.val)
    while(L3.next is not None):
        print(L3.val)
        L3 = L3.next

if __name__ == '__main__':
    main()