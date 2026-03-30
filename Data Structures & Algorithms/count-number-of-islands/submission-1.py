class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs, remove visited land
        m,n = len(grid),len(grid[0])
        # unvisited = [[True for _ in range(n)] for _ in range(m)]

        def dfs(i,j) -> None:
            # unvisited[i][j] = False
            grid[i][j] = '0'
            if i-1 >= 0:
                if grid[i-1][j]=='1':
                    dfs(i-1,j)
            if i+1 < m:
                if grid[i+1][j]=='1':
                    dfs(i+1,j)
            if j-1 >= 0:
                if grid[i][j-1]=='1':
                    dfs(i,j-1)
            if j+1 < n:
                if grid[i][j+1]=='1':
                    dfs(i,j+1)
            return
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    res +=1
        return res
