# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 22:58:33 2019

@author: zhengstars
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        
        # sort according to the first number in intervals
        intervals.sort(key = lambda x: x.start)
        
        # put the first interval into the result list
        res = [intervals[0]]
        
        for i, e in enumerate(intervals, start = 1):
            # final element in res[（start, end）] >= e.start then merge
            if e.start <= res[-1].end:
                res[-1].end = max(res[-1].end, e.end)
            else:
                res.append(e)
        return res
    