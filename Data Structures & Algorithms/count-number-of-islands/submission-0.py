class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r,c=len(grid),len(grid[0])
        visited=set()
        island=0

        def dfs(i,j):
            if i<0 or i>=r or j<0 or j>=c or grid[i][j]=="0":
                return 1
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            s=dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
            return s
        for k in range(r):
            for m in range(c):
                if grid[k][m]=="1":
                    if dfs(k,m):
                        island+=1
        return island

        