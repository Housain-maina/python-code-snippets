from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(
        f"""
            +-------+-------+-------+
            |       |       |       |
            |   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
            |       |       |       |
            +-------+-------+-------+
            """
    )


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            move = int(input("enter your move: "))
            if move > 0 and move < 10:
                if move in board[0]:
                    position = board[0].index(move)
                    board[0][position] = "O"
                    break
                elif move in board[1]:
                    position = board[1].index(move)
                    board[1][position] = "O"
                    break
                elif move in board[2]:
                    position = board[2].index(move)
                    board[2][position] = "O"
                    break
                else:
                    print("Field already occupied")
                    continue
            else:
                print("Invalid field number.")
                continue
        except ValueError:
            print("Invalid input type.")
            continue


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for i in range(3):
        for j in range(3):
            if isinstance(board[i][j], int):
                free_fields.append((i, j))
    return free_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return str(sign + " wins")
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return str(sign + " wins")
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return str(sign + " wins")
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return str(sign + " wins")
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return str(sign + " wins")
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return str(sign + " wins")
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return str(sign + " wins")
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return str(sign + " wins")
    else:
        return str(sign + " lose")


def draw_move(board):
    # The function draws the computer's move and updates the board.
    while True:
        move = randrange(1, 10)
        if move in board[0]:
            position = board[0].index(move)
            board[0][position] = "X"
            break
        elif move in board[1]:
            position = board[1].index(move)
            board[1][position] = "X"
            break
        elif move in board[2]:
            position = board[2].index(move)
            board[2][position] = "X"
            break
        else:
            continue


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
counter = 0
while True:
    if counter == 0:
        display_board(board)
        board[1][1] = "X"
        counter += 2
        continue
    else:
        if counter % 2 == 0:
            if victory_for(board, "O") == "O wins":
                display_board(board)
                print("You won.")
                break
            elif victory_for(board, "X") == "X wins":
                display_board(board)
                print("You lose.")
                break
            elif (
                victory_for(board, "O") != "O wins"
                and victory_for(board, "X") != "X wins"
                and len(make_list_of_free_fields(board)) == 0
            ):
                display_board(board)
                print("Game ended in a tie.")
                break
            else:
                display_board(board)
                enter_move(board)
                counter += 1
                continue

        elif counter > 1 and counter % 2 != 2:
            if victory_for(board, "O") == "O wins":
                display_board(board)
                print("You won.")
                break
            elif victory_for(board, "X") == "X wins":
                display_board(board)
                print("You lose.")
                break
            elif (
                victory_for(board, "O") != "O wins"
                and victory_for(board, "X") != "X wins"
                and len(make_list_of_free_fields(board)) == 0
            ):
                display_board(board)
                print("Game ended in a tie.")
                break
            else:
                display_board(board)
                draw_move(board)
                counter += 1
                continue
