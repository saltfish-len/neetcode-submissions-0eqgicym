class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs, remove visited land
        m,n = len(grid),len(grid[0])
        # unvisited = [[True for _ in range(n)] for _ in range(m)]

        def dfs(i,j,size):
            # unvisited[i][j] = False
            grid[i][j] = 0
            size+=1
            if i-1 >= 0:
                if grid[i-1][j]==1:
                    size=dfs(i-1,j,size)
            if i+1 < m:
                if grid[i+1][j]==1:
                    size=dfs(i+1,j,size)
            if j-1 >= 0:
                if grid[i][j-1]==1:
                    size=dfs(i,j-1,size)
            if j+1 < n:
                if grid[i][j+1]==1:
                    size=dfs(i,j+1,size)
            return size
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(dfs(i,j,0),res)
                    
        return res