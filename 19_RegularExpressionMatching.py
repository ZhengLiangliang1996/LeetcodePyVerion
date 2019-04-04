#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:43:40 2019

@author: liangliang
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # case 
        flag = True
        i = 0
        j = 0
        while(i < len(s) and j < len(p)):
            # same symbol
            if s[i] == p[j]:
                i = i + 1
                j = j + 1
            else:
                if p[j] == '.':
                    i = i + 1
                    j = j + 1
                elif p[i] == '*':
                    #need to match until the next symbol appear
                    
                    i = i + 1
                else:
                    flag = False
                    break
        return flag
                    

def main():
    S = Solution()
    a = S.isMatch("aab", "c*a*b")
    print(a)

if __name__ == '__main__':
    main()