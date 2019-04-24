#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:11:01 2019

@author: liangliang
"""

class Solution(object):
    def letterCombinations(self, a, b):
        """
        :type digits: str
        :rtype: List[str]
        """
        if b == []:
            return []
        
        resSub = []
        resSub.append(b[0])
        res = []
        S = set()
        countFirstNumber = 1
        for i in range(a):
            if b[i] in resSub:
                countFirstNumber = countFirstNumber + 1
        res.append(resSub)
        
        for j in range(countFirst-1,a):
            i = countFirstNumber
            resSub = []
            while(i >0 ):
                resSub.append(b[j])
            res.append(resSub)
                
                
            
            
            
                
            
        
    
def main():
    S = Solution()
    a = 6
    b = [1,1,2,2,3,3]
    a = S.letterCombinations(a, b)
    print(a)
    
if __name__ == "__main__":
    main()