# class Solution:
board = [[".","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]




def solveSudoku(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    def isValid(board, i, j, num) -> bool:

        for k in range(9):
            if board[i][k] == str(num): return False
            if board[k][j] == str(num): return False
            if board[(i//3)*3 + k//3][(j//3)*3 + k%3] == str(num): return False

        return True
        
        # for x in range(m):
        #     if board[x][j] == str(num):
        #         return False

        # for y in range(n):
        #     if board[i][y] == str(num):
        #         return False

        # leftup_x = (i // 3) * 3
        # leftup_y = (j // 3) * 3

        # for x in range(leftup_x, leftup_x + 3):
        #     for y in range(leftup_y, leftup_y + 3):
        #         if board[x][y] == str(num):
        #             return False

        # return True

    def backtrack(board, i, j) -> bool:
        if j == n: # 换行
            return backtrack(board, i+1, 0)

        if i == m: # 找到一组可行解
            return True

        if board[i][j] != '.': # 如果已经预先设有了数字
            return backtrack(board, i, j+1)

        for num in range(1, 10):
            print(i, j, num)
            # print(isValid(board, i, j, num))
            if isValid(board, i, j, num):
                board[i][j] = str(num)

                if backtrack(board, i, j+1):
                    return True

                board[i][j] = '.'
                
        return False

    m = len(board)
    n = len(board[0])

    if backtrack(board, 0, 0):
        return board

solution = solveSudoku(board=board)
print(solution)