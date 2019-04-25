#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:17:38 2019
https://blog.csdn.net/ms961516792/article/details/88596440
@author: liangliang
"""

class Solution(object):
    def filterSTring(self, string):
        """
        :type digits: str
        :rtype: List[str]
        """
        n = len(string)
        i = 0
        while(i < n):
            next1 = i + 1
            while string[next1] == '#' and next1 < n:
                next1 = next1 + 1
            next2 = next1 + 1
            while string[next2] == '#' and next2 < n:
                next2 = next2 + 1
            next3 = next2 + 1
            while string[next3] == '#' and next3 < n:
                next3 = next3 + 1
            
            if(string[i] == string[next1] and string[next1]==string[next2]):
                string = string[:i] + '#' + string[i + 1:]
                i = i + 1
                continue
            elif(string[i] == string[next1] and string[next2]==string[next3]):
                string = string[:next2] + '#' + string[next2 + 1:]
                continue
            else:
                i = i + 1
                continue
            
        print(string)
            
        
                
def main():
    S = Solution()
    a = S.filterSTring('aabb')

if __name__ == "__main__":
    main()
