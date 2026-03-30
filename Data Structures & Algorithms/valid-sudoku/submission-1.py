class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for i in range(9):
            check = defaultdict(int)
            for j in range(9):
                if board[i][j]!='.':
                    if check[board[i][j]] >= 1: return False
                    check[board[i][j]] += 1
        # col
        for j in range(9):
            check = defaultdict(int)
            for i in range(9):
                if board[i][j]!='.':
                    if check[board[i][j]] >= 1: return False
                    check[board[i][j]] += 1

        # cube
        for i_base in range(0,9,3,):
            for j_base in range(0,9,3):
                # top left corner
                check = defaultdict(int)
                for i in range(i_base,i_base+3):
                    for j in range(j_base,j_base+3):
                        if board[i][j]!='.':
                            if check[board[i][j]] >= 1: return False
                            check[board[i][j]] += 1
        
        return True