class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs, add rotten to queue
        q = []
        m,n = len(grid),len(grid[0])
        freshcount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshcount += 1
                elif grid[i][j] == 2:
                    q.append([i,j])
        move = [[1,0],[-1,0],[0,1],[0,-1]]
        time = 0
        while freshcount > 0 and q:
            l = len(q)
            for _ in range(l):
                x, y = q.pop(0)
                for dx,dy in move:
                    if 0 <= x+dx < m and 0 <= y+dy < n:
                        if grid[x+dx][y+dy] == 1:
                            grid[x+dx][y+dy] = 2
                            q.append([x+dx,y+dy])
                            freshcount -= 1
            time += 1

        if freshcount > 0:
            return -1
        return time
                    