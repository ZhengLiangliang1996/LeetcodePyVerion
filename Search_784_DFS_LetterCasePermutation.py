#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:51:38 2019

@author: liangliang
"""

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        length = len(S)
        res = []
        def dfs(num, string, res):
            if num == length:
                res.append(''.join(string))
                return 
            # move to the next whatever(actually this is the case when it is number)
            dfs(num + 1, string, res)
            # this is the case when this is not alphabet, only the line up here will be run 
            # if all string is number, then only run dfs n times O(n)
            if not string[num].isalpha(): return 
            # underwise, run the dfs again, make it to upper or lower case
            string[num] = chr(ord(string[num]) ^ (1 << 5))
            dfs(num + 1, string, res)
            # turn it back
            string[num] = chr(ord(string[num]) ^ (1 << 5))
        
        dfs(0, list(S), res)
        return res
            
def main():
    S = Solution()
    a = S.letterCasePermutation('a1z2')
    print(a)
    
if __name__ == "__main__":
    main()
    