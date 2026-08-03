class Solution:
    def orangesRotting(self, m: List[List[int]]) -> int:
        R,C=len(m),len(m[0])
        visited=set()
        q=deque()
        f=0
        def addroom(i,j):
            nonlocal f
            if i<0 or i>=R or j<0 or j>=C or (i,j) in visited or m[i][j]==2 or m[i][j]==0:
                return
            visited.add((i,j))
            q.append([i,j])
            f=f-1
        for i in range(R):
            for j in range(C):
                if m[i][j]==2:
                    q.append([i,j])
                    visited.add((i,j))
                if m[i][j]==1:
                    f+=1

        Rmin=0
        while q and f>0:
            for l in range(len(q)):
                i,j=q.popleft()
                m[i][j]=2
                addroom(i+1,j)
                addroom(i-1,j)
                addroom(i,j+1)
                addroom(i,j-1)
        
            Rmin+=1
        return Rmin if f==0 else -1


        