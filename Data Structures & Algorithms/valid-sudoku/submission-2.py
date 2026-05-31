class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Check Columns
        for i in range(9):
            count_col = {}
            for j in range(9):
                val = board[j][i]
                if val != ".":
                    if val in count_col: return False
                    count_col[val] = 1

        # 2. Check Rows
        for i in range(9):
            count_row = {}
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    if val in count_row: return False
                    count_row[val] = 1

        # 3. Check Squares (The fix we discussed)
        for r_start in range(0, 9, 3):
            for c_start in range(0, 9, 3):
                count_square = {}
                for i in range(3):
                    for j in range(3):
                        val = board[r_start + i][c_start + j]
                        if val != ".":
                            if val in count_square: return False
                            count_square[val] = 1
        
        # If we reached here, no duplicates were found anywhere
        return True