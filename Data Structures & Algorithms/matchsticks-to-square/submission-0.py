class Solution:
    def makesquare(self, m: List[int]) -> bool:
        length=sum(m)//4
        sides=[0]*4

        if sum(m)/4!=length:
            return False
        m.sort(reverse=True)
        def dfs(i):
            if i==len(m):
                return True
            
            for j in range(4):
                if sides[j]+m[i]<=length:
                    sides[j]+=m[i]
                    if dfs(i+1):
                        return True
                    sides[j]-=m[i]
            return False
        return dfs(0)
        