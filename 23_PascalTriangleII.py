#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:42:37 2019

@author: liangliang
"""

def getRow(rowIndex):
        ps=[1]
        for i in range(rowIndex):
            
            ps=[sum(x) for x in zip([0]+ps, ps+[0])]
            print(ps)
        #print(ps)
        return ps
    
def main():
    getRow(2)
    
if __name__ == "__main__":
    main()
        