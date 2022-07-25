EMPTY = "_"
ROOK = "ROOK"
PAWN = "PAWN"
board = []

for _ in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[4][2] = ROOK
board[3][4] = PAWN

print(board)
