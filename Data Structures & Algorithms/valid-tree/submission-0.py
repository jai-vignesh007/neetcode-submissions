class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        pcmap={i:[] for i in range(n)}
        for p,c in edges:
            pcmap[p].append(c)
            pcmap[c].append(p)
        
        visit=set()

        def dfs(i,prev):
            if i in visit:
                return False
            visit.add(i)

            for c in pcmap[i]:
                if c == prev:
                    continue
                if not dfs(c,i):
                    return False
            return True



        return dfs(0,-1) and len(visit)==n