class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            #print(f'row_{i}')
            #print(board[i])
            seen=[]
            for number in range(len(board[i])):
                cell_value =board[i][number]
                if cell_value !='.':
                    if cell_value in seen:
                        return False
                        break
                    else: 
                        seen.append(cell_value)
        #print(check_row_non_repeat_status)
        for i in range(len(board)):
            #print(f'column_{i}')
            seen=[]
            for j in range(len(board)):
                #print(board[j][i])
                if board[j][i] !='.':
                    if board[j][i] in seen:
                        return False
                        break
                    else: 
                        seen.append(board[j][i])
        #print(check_column_non_repeat_status)
        for box_row in range(3):       # 方塊的橫向座標 0, 1, 2
            for box_col in range(3):   # 方塊的縱向座標 0, 1, 2
                seen = []              # 💡 關鍵：每個新方塊都要有一個獨立的看過清單
                # 計算出這個方塊在 9x9 盤面上的真正「左上角起點」
                start_row = box_row * 3
                start_col = box_col * 3
                # 接下來，用迴圈走訪這個方塊裡面的 9 個格子
                for r in range(start_row, start_row + 3):
                    for c in range(start_col, start_col + 3):
                        cell_value = board[r][c]
                        if cell_value !='.':
                            if cell_value in seen:
                                return False
                                break
                            else: 
                                seen.append(cell_value)
        return True




