#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 21:24:03 2019

@author: liangliang
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        if strs == []:
            return result 
        first_strs = strs[0]
        if len(strs) == 1:
            return first_strs
        if "" in strs:
            return ""
        
        for i in range(len(first_strs)):
            flag = True
            for j in range(1, len(strs)):
                print(i,j)
                if(i >= len(strs[j])):
                    flag = False
                    break
                
                if strs[j][i] != strs[j-1][i]:
                    flag = False
                    break
                
                if(strs[j][i] == strs[j-1][i] and j == (len(strs) -1) and flag == True):
                    result = result + strs[j][i]
            if flag == False:
                break
            
        return result


def main():
    S = Solution()
    a = S.longestCommonPrefix(["a"])
    print(a)

if __name__ == '__main__':
    main()
        