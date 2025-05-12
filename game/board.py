def reset_board():
    return [['' for _ in range(3)] for _ in range(3)]

def check_win(board, player):
    # Verificar filas
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Verificar columnas
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Verificar diagonales
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][3 - i - 1] == player for i in range(3)]):
        return True
    return False

def check_tie(board):
    for row in board:
        if '' in row:
            return False
    return True
