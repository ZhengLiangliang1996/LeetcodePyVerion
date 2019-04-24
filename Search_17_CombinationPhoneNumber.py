#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:59:45 2019

@author: liangliang
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #边境
        if digits == "":
            return []
        
        dict = {'2':['a', 'b','c'],
                '3':['d', 'e', 'f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                 }
        #including the length of string and string and return result 
        length = len(digits)
        def dfs(num, string, res):
            if num == length:
                # when one is reached, then return to end current stack of recursion
                res.append(string)
                return
            for i in dict[digits[num]]:
                dfs(num+1, string+i,res)
       
        res = []
        dfs(0, '', res)
        return res
        
    
def main():
    S = Solution()
    a = S.letterCombinations("23")
    print(a)
    
if __name__ == "__main__":
    main()