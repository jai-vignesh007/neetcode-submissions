class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ic=defaultdict(int)
        og=defaultdict(int)
        for a,b in trust:
            og[a]+=1
            ic[b]+=1
        for i in range(1,n+1):
            if ic[i]==n-1 and og[i]==0:
                return i
        return -1