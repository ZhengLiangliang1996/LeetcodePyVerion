#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:14:14 2019

@author: liangliang
"""

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        #first get how many left paren and right paren should be deleted
        l = 0
        r = 0
        for i in s:
            # detect from left
            l = l + (i == '(')
            # if 0, then its is a right, +1 right
            if (l == 0):
                r = r + (i == ')')
            # else minus 1
            else:
                l = l - (i == ')')

        ##################
        # check valid when result is searched to the end
        ##################
        def isValid(s):
            count = 0
            for ch in s:
                if ch == '(': count = count + 1
                if ch == ')': count = count - 1
                if count < 0: return False
            return count == 0
        
        
        
        ##################
        # dfs
        ##################
        # start means that if we found one and delete, next round of 
        # the recursion we start from the place where we deleted last time
        def dfs(s, start, l, r, res):
            # end condition
            if l == 0 and r == 0:
                if isValid(s): 
                    res.append(s)
                    return 
                
            
            for i in range(start, len(s)):
                 # We only remove the first parenthes if there are consecutive ones to avoid duplications.
                 # pruning
                 if i != start and s[i] == s[i - 1]: 
                     continue
                 # only concerning when element is parentheses
                 if (s[i] == '(' or s[i] == ')'):
                     # create curr since s will be changed :REF
                     curr = s
                     # delete one parenthese
                     curr = curr[:i] + curr[i + 1:]
                     if r > 0:
                         dfs(curr, i, l, r - 1, res)
                         
                     elif l > 0:
                         dfs(curr, i, l - 1, r, res)
        res = []
        dfs(s, 0, l, r, res) 
        return res
                     
def main():
    S = Solution()
    a = S.removeInvalidParentheses("(a)())()")
    print(a)
    
if __name__ == "__main__":
    main()