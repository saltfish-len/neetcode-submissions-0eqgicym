class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        direction = [(-1,0),(1,0),(0,1),(0,-1)]
        lw = len(word)
        
        def dfs(r,c,i):
            # i: s[i:]
            res = False
            if board[r][c] == word[i]:
                # move 
                if i == lw -1:
                    return True
                board[r][c] = "#"
                for dx,dy in direction:
                    x, y = r+dx, c+dy
                    if 0 <= x < m and 0 <= y < n and board[x][y] != "#":
                        res = res or dfs(x,y,i+1) 
                board[r][c] = word[i]
            
            return res
        res = False
        for i in range(m):
            for j in range(n):
                res = res or dfs(i,j,0)
        
        return res