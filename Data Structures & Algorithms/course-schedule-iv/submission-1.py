class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj={i:[]for i in range(numCourses)}
        prereqmap={}
        for p,c in prerequisites:
            adj[c].append(p)
        

        def dfs(crs):
            if  crs not in prereqmap:
                prereqmap[crs]=set()
                for p in adj[crs]:
                    prereqmap[crs]|=dfs(p)
                prereqmap[crs].add(crs)
            
            return prereqmap[crs]
        prereqmap={}
        for crs in range(numCourses):
            dfs(crs)
        res=[]
        for u,v in queries:
            res.append(u in prereqmap[v])
        return res
