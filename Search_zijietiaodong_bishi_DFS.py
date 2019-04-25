#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:48:00 2019

@author: liangliang
"""
class Solution(object):
    def getData(self, m, n, audience):
        """
        :type digits: str
        :rtype: List[str]
        """
        #边境
        
        visited = [[0 for x in range(m)] for y in range(n)] 
        
        def dfs(x, y, m, n,audience, visited):
            # end condition
            if x < 0 or x >= m or y < 0 or y >= n:
                return 0
            elif audience[x][y] == 1 and visited[x][y] == 0:
                visited[x][y] = 1;
                n1 = dfs(x - 1, y, m, n, audience, visited) + dfs(x + 1, y, m, n, audience, visited)
                n2 = dfs(x, y - 1, m, n, audience, visited) + dfs(x, y + 1, m, n, audience, visited)
                n3 = dfs(x - 1, y - 1, m, n, audience, visited) + dfs(x - 1, y + 1, m, n, audience, visited)
                n4 = dfs(x + 1, y - 1, m, n, audience, visited) + dfs(x + 1, y + 1, m, n, audience, visited)
                return n1+n2+n3+n4+1 
            else:
                return 0
        
        res = []
        for i in range(m):
            for j in range(n):
                if(audience[i][j]==1 and visited[i][j]==0):
                        a = dfs(i, j, m, n, audience, visited)
                        res.append(a)
        
        return res
                
                
def main():
    S = Solution()
    audience = [
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,1,1,0,1,0,0,0],
           [0,1,0,0,0,0,0,1,0,1],
           [1,0,0,0,0,0,0,0,1,1],
           [0,0,0,1,1,1,0,0,0,1],
           [0,0,0,0,0,0,1,0,1,1],
           [0,1,1,0,0,0,0,0,0,0],
           [0,0,0,1,0,1,0,0,0,0],
           [0,0,1,0,0,1,0,0,0,0],
           [0,1,0,0,0,0,0,0,0,0]
            ]
    a = S.getData(10, 10, audience)
    print(len(a))
    print(max(a))
    print(a)
    
if __name__ == "__main__":
    main()
