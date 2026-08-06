class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj={i:[]for i in range(n)}
        visit=[False]*n
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        

        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei]=True
                    dfs(nei)

            
        
        i=0
        for node in range(n):
            if not visit[node]:
                visit[node]=True
                dfs(node)
                i+=1
        return i


        