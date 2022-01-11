def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [[ '.','.','.' ],[ '.','.','.' ],[ '.','.','.' ]]
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row = 0
    col = 0
    taken_coordinates = set()
    coordinates = input("Provide coordinates: ").upper()
    row = coordinates[0]
    col = int(coordinates[1])
    while coordinates not in {"A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"}:
        print("Please enter valid coordinates (A1, A2, A3, B1, B2, B3, C1, C2, C3): ")
        coordinates = input("Provide coordinates: ").upper()
    row_and_col = (coordinates[0], int(coordinates[1]))
    taken_coordinates.add(coordinates)
    print(taken_coordinates)
    return row_and_col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    conv_row = 0
    if row == "A":
        conv_row = 0
    elif row == "B":
        conv_row = 1
    elif row == "C":
        conv_row = 2
    while True:
        if player % 2 == 0 and board[conv_row][col-1] == '.':
            board[conv_row][col-1] = 'X'
            player += 1
            return player
        if player % 2 == 1 and board[conv_row][col-1] == '.':
            board[conv_row][col-1] = '0'
            player += 1
            return player
        elif board[conv_row][col-1] != '.': 
            print("Those coordinates are occupied, please choose an empty one.")
            return player
    #return print(board)

def rows(board):
    for i in range(3):
        x_count = 0
        o_count = 0
        for j in range(3):
            if board[i][j] == "X":
                x_count += 1
            elif board[i][j] == "0":
                o_count += 1
        if x_count == 3 or o_count == 3:
            return True
    return False

def cols(board):
    for i in range(3):
        x_count = 0
        o_count = 0
        for j in range(3):
            if board[j][i] == "X":
                x_count += 1
            elif board[j][i] == "0":
                o_count += 1
        if x_count == 3 or o_count == 3:
            return True
    return False

def diagonals(board):
    x_count = 0
    o_count = 0
    x_count2 = 0
    o_count2 = 0
    for i in range(3):
        if board[i][i] == "X":
            x_count += 1
        elif board[i][i] == "0":
            o_count += 1
        if board[i][2-i] == "X":
            x_count2 += 1
        elif board[i][2-i] == "0":
            o_count2 += 1
    if x_count == 3 or o_count == 3 or x_count2 == 3 or o_count == 3:
        return True     
    else:
        return False
        


def has_won(board, active_player):
    """Returns True if player has won the game."""
    return rows(board) or cols(board) or diagonals(board)


def is_full(board):
    """Returns True if board is full."""
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    pass


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    print(f"The winner is Player {(winner % 2) + 1}")


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    #get_move(board, 1)
    active_player = 1
    while not has_won(board, active_player):       
        move = get_move(board, 1)
        row = move[0]
        col = move[1]
        active_player = mark(board, active_player, row, col)
        print(board)
    winner = active_player
    print_result(winner)
   

def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
