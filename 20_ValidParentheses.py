#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:47:58 2019

@author: liangliang
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        v=[]
        a=['(','{','[']
        for i in range(len(s)):
            if s[i] in a:
                v.append(s[i])
                continue
            elif s[i]==')':
                if len(v)==0 or v.pop()!='(':
                    return False
            elif s[i]==']':
                if len(v)==0 or v.pop()!='[':
                    return False           
            elif s[i]=='}':
                if len(v)==0 or v.pop()!='{':
                    return False         
        return len(v)==0
