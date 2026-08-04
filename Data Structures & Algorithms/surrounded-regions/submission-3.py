class Solution:
    def solve(self, m: List[List[str]]) -> None:
        R,C=len(m),len(m[0])
        def dfs(i,j):
            if i<0 or i>=R or j<0 or j>=C  or m[i][j]!="O" :
                return
            m[i][j]="T"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            return 
        for i in range(R):
            for j in range(C):
                if m[i][j]=="O" and (i in [0,R-1] or j in [0,C-1]) :
                    dfs(i,j)

        for i in range(R):
            for j in range(C):
                if m[i][j]!="T":
                    m[i][j]="X"
                if m[i][j]=="T":
                    m[i][j]="O"
        
        