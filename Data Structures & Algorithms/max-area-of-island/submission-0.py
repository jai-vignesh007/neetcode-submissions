class Solution:
    def maxAreaOfIsland(self, m: List[List[int]]) -> int:
        visited=set()
        R,C=len(m),len(m[0])
        maxa=0
        def dfs(i,j):
            if i<0 or i>=R or j<0 or j>=C or (i,j) in visited or m[i][j]==0:
                return 0
            visited.add((i,j))
            return (1+dfs(i-1,j)+dfs(i+1,j)+dfs(i,j-1)+dfs(i,j+1))
            
        for i in range(R):
            for j in range(C):
                if m[i][j]:
                    maxa=max(maxa,dfs(i,j))
        return maxa
        