class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        m,n = len(grid), len(grid[0])

        visited = [[False] * n for _ in range(m)]

        def dfs(i, j):
            visited[i][j] = True
            # up
            if i-1 >= 0:
                if not visited[i-1][j]:
                    if grid[i-1][j] == "1":
                        dfs(i-1, j)
            # down
            if i+1 < m:
                if not visited[i+1][j]:
                    if grid[i+1][j] == "1":
                        dfs(i+1, j)
            # left
            if j-1 >= 0:
                if not visited[i][j-1]:
                    if grid[i][j-1] == "1":
                        dfs(i,j-1)
            # right
            if j+1 < n:
                if not visited[i][j+1]:
                    if grid[i][j+1] == "1":
                        dfs(i,j+1)
        res = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i,j)
                    res += 1
        return res