class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R,C=len(heights),len(heights[0])
        pac,alt=set(),set()

        def dfs(i,j,visit,prevheights):
            if i<0 or i>=R or j<0 or j>=C or (i,j) in visit or prevheights > heights[i][j]:
                return 
            visit.add((i,j))
            dfs(i+1,j,visit,heights[i][j])
            dfs(i-1,j,visit,heights[i][j])
            dfs(i,j+1,visit,heights[i][j])
            dfs(i,j-1,visit,heights[i][j])
            return visit


        for c in range(C):
            dfs(0,c,pac,heights[0][c])
            dfs(R-1,c,alt,heights[R-1][c])
        
        for r in range(R):
            dfs(r,0,pac,heights[r][0])
            dfs(r,C-1,alt,heights[r][C-1])
        res=[]
        for i in range(R):
            for j in range(C):
                if (i,j) in pac and (i,j) in alt:
                    res.append([i,j])
        return res



        