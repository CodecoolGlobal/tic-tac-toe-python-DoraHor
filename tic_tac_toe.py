def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [[ '.','.','.' ],[ '.','.','.' ],[ '.','.','.' ]]
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row = 0
    col = 0
    taken_coordinates = set()
    coordinates = input("provide coordinates: ").upper()
    row = coordinates[0]
    col = int(coordinates[1])
    while coordinates not in {"A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"} or coordinates in taken_coordinates:
        print("Please enter valid coordinates (A1, A2, A3, B1, B2, B3, C1, C2, C3): ")
        coordinates = input("provide coordinates: ").upper()
        

    # while row not in {"a", "b", "c"}:
    #     print("Please enter A, B or C")
    #     row = input("Row: ").lower()
    # while col not in {1, 2, 3}:
    #     print("Please enter 1, 2 or 3")
    #     col = int(input("Col: "))
    # row_and_col = (row, col)
    # while row_and_col not in taken_coordinates:
    #     print("Those coordinates are already taken.")
    row_and_col = (coordinates[0], int(coordinates[1]))
    taken_coordinates.add(coordinates)
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
    board[conv_row][col-1] = 'X'
    return print(board)



def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    pass


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    #get_move(board, 1)
    move = get_move(board, 1)
    row = move[0]
    col = move[1]
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
