def solution(board):
    def win(p):
        for i in range(3):
            if all(board[i][j] == p for j in range(3)): return True
            if all(board[j][i] == p for j in range(3)): return True
        if all(board[i][i] == p for i in range(3)): return True
        if all(board[i][2 - i] == p for i in range(3)): return True
        return False

    o = sum(row.count('O') for row in board)
    x = sum(row.count('X') for row in board)
    ow = win('O')
    xw = win('X')

    if not (o == x or o == x + 1): return 0
    if ow and xw: return 0
    if ow and o != x + 1: return 0
    if xw and o != x: return 0
    return 1
