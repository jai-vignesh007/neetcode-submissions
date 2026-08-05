class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[List[int]]:
        # Step 1: Build adjacency list (course -> list of prerequisites)
        prereq = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            # If node is in current path -> Cycle detected!
            if crs in cycle:
                return False
            # If node was already fully processed -> Skip
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            visit.add(crs)
            # Add to output ONLY after all prerequisites are added
            output.append(crs)
            return True

        # Run DFS on all nodes (handles disconnected components)
        for c in range(numCourses):
            if not dfs(c):
                return []  # Return [] if cycle exists

        return output