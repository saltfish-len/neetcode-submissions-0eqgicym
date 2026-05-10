class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS from treasure
        sources = []
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    sources.append((i,j))
        visited = set()
        valid = lambda i,j: 0<=i<m and 0<=j<n and grid[i][j] != -1 and (i,j) not in visited
        for si,sj in sources:
            que = [[si,sj,0]]
            visited = set()
            while que:
                i,j,step = que.pop(0)
                cur = grid[i][j]
                grid[i][j] = min(step, cur)
                    
                ni,nj = i+1,j
                if valid(ni,nj):
                    que.append([ni,nj,step+1])
                    visited.add((ni,nj))
                ni,nj = i-1,j
                if valid(ni,nj):
                    que.append([ni,nj,step+1])
                    visited.add((ni,nj))
                ni,nj = i,j+1
                if valid(ni,nj):
                    que.append([ni,nj,step+1])
                    visited.add((ni,nj))
                ni,nj = i,j-1
                if valid(ni,nj):
                    que.append([ni,nj,step+1])
                    visited.add((ni,nj))
        return


