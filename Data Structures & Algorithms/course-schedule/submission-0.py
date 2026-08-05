class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        PrevMap={i:[] for i in range(numCourses)}
        for crs,prev in prerequisites:
            PrevMap[crs].append(prev)
        visited=set()
        def dfs(crs):
            if crs in visited:
                return False
            if PrevMap[crs]==[]:
                return True
            
            visited.add(crs)
            for pre in PrevMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            PrevMap[crs]=[]
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        