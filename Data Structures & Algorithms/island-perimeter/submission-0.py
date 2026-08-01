class Solution:
    def islandPerimeter(self, m: List[List[int]]) -> int:
        visit=set()
        R, C = len(m), len(m[0])

        def dfs(i, j):
            if i<0 or i>=R or j<0 or j>=C or m[i][j]==0 :
                return 1
            if (i,j) in visit:
                return 0
            visit.add((i,j))
            s=dfs(i+1,j)+dfs(i-1,j)+dfs(i,j-1)+dfs(i,j+1)
            return s
        for i in range(R):
            for j in range(C):
                if m[i][j]:
                    return dfs(i,j)
        return 0

        