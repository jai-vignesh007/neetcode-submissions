class Solution:
    def partition(self, s: str) -> List[List[str]]:
        part=[]
        res=[]

        def dfs(i):
            if i>=len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                if self.ispoli(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
    def ispoli(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            r-=1
            l+=1
        return True