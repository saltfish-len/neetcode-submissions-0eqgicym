class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort
        # dfs cycle
        q = []
        visiting = set()
        edge = defaultdict(list)
        for s,d in prerequisites:
            edge[s].append(d)
        
        def dfs(v):
            if v in visiting:
                return False
            visiting.add(v)
            res = True
            for d in edge[v]:
                if not dfs(d):
                    return False
            visiting.remove(v)
            edge[v] = []
            return res

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        
        
