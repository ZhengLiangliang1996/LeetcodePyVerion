#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 23:39:58 2019

@author: liangliang
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Python rstrip() 删除 string 字符串末尾的指定字符（默认为空格）
        return len(s.rstrip().split(' ')[-1])
    
def main():
    S = Solution()
    a = S.lengthOfLastWord("         ")
    print(a)

if __name__ == '__main__':
    main()
        