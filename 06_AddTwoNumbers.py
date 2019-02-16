#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 21:57:18 2019

@author: liangliang
"""

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum1 = ""
        sum2 = ""
        while (l1 != None):
            sum1 += str(l1.val)
            l1 = l1.next
            
        while (l2 != None):
            sum2 += str(l2.val)
            l2 = l2.next
        
        #transfer string to int 
        # meaning of ::-1
        # a = '1232'
        # a[::-1]  - > '2321'
        data1 = int(sum1[::-1])
        data2 = int(sum2[::-1])
        
        ans = str(data1 + data2)[::-1]
        
        ret = []
        for i in range(len(ans)):
            ret.append(ListNode(int(ans[i])))

        for i in range(len(ret) - 1):
            ret[i].next = ret[i+1]

        return ret[0]
            
        
def main():

    
    S = Solution()
    lll1 = S.addTwoNumbers(l1, ll1)
    print(lll1.val)
    
if __name__ == '__main__':
    main()
        