#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:51:45 2019

@author: liangliang
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def dfs(left, right, string, res):
            if left == 0 and right == 0:
                res.append(string)
                return 
            # left > 0
            if left > 0:
                dfs(left - 1, right, string + "(", res)
            if left < right:
                dfs(left, right - 1, string + ")", res)
                    
        dfs(n, n, "", res)
        return res

def main():
    S = Solution()
    a = S.generateParenthesis(3)
    print(a)
    
if __name__ == "__main__":
    main()
    