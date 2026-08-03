class Solution:
    def islandsAndTreasure(self, m: List[List[int]]) -> None:
        visited=set()
        R,C=len(m),len(m[0])
        q=deque()
        def addroom(i,j):
            if i<0 or i>=R or j<0 or j>=C or (i,j) in visited or m[i][j]==-1:
                return
            visited.add((i,j))
            q.append([i,j])
        for i in range(R):
            for j in range(C):
                if m[i][j]==0:
                    q.append([i,j])
                    visited.add((i,j))

        dist=0
        while q:
            for l in range(len(q)):
                i,j=q.popleft()
                m[i][j]=dist
                addroom(i+1,j)
                addroom(i-1,j)
                addroom(i,j+1)
                addroom(i,j-1)
            dist+=1