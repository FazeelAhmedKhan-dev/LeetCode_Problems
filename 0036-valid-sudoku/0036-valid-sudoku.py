from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        grid = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in grid[(i//3, j//3)]:
                    return False
                
                grid[(i//3, j//3)].add(board[i][j])

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
        return True
