class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo={}
        n=len(obstacleGrid[0])
        m=len(obstacleGrid)
        def dfs(i,j):
            if i>=m or j>=n or obstacleGrid[i][j]==1:
                return 0
            if i==m-1 and n-1==j:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)]=dfs(i+1,j)+dfs(i,j+1)
            return memo[(i,j)]

        return dfs(0,0)
        