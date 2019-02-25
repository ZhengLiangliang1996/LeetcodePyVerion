#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:42:50 2019

@author: liangliang
"""

graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

visited = []

def dfs(graph, node, visted):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visted)
    return visited

visited = dfs(graph1, 'A', [])
print(visited)