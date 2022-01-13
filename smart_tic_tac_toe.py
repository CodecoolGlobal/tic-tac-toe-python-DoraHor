import random
from time import sleep

def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [[ '.','.','.' ],[ '.','.','.' ],[ '.','.','.' ]]
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row = 0
    col = 0
    coordinates = input("\n Provide coordinates: ").upper()
    if coordinates.lower() == 'quit':
        print("\n Thanks for playing, goodbye. \n ")
        exit()
    else:
        try:
            row = coordinates[0]
            col = int(coordinates[1])
        except (IndexError, ValueError):
            pass
        while coordinates not in {"A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"}:
            print("\n Please enter valid coordinates (A1, A2, A3, B1, B2, B3, C1, C2, C3): ")
            coordinates = input("\n Provide coordinates: ").upper()
        row_and_col = (coordinates[0], int(coordinates[1]))
        return row_and_col


def get_ai_move(board):
    """Returns the coordinates of a valid move for player on board."""
    if is_full(board):
        return None
    else:
        while True:
            random_row = random.randint(0,2)
            random_col = random.randint(0,2)
            if board[random_row][random_col] == '.':
                row_and_col = (random_row, random_col)
                print(f" AI's move: {random_row + 1}, {random_col + 1}")
                return row_and_col

def smart_ai_rows(board):
    for i in range(3):
        x_count = 0
        o_count = 0
        for j in range(3):
            if board[i][j] == "X":
                x_count += 1
                
            elif board[i][j] == "0":
                o_count += 1
        try:
            empty = (i, board[i].index('.'))
        except ValueError:
            pass
        try:
            if x_count == 2 or o_count == 2:
                return True, empty
        except UnboundLocalError:
            return False, None
    return False, None

def smart_ai_cols(board):
    for i in range(3):
        x_count = 0
        o_count = 0
        for j in range(3):
            if board[j][i] == "X":
                x_count += 1
                   
            elif board[j][i] == "0":
                o_count += 1
        try:
            empty = (board[j].index('.'), j)
        except ValueError:
            pass
        try:
            if x_count == 2 or o_count == 2:
                return True, empty
        except UnboundLocalError:
            return False, None
    return False, None

def smart_ai_diag(board):
    x_count = 0
    o_count = 0
    x_count2 = 0
    o_count2 = 0
    for i in range(3):
        if board[i][i] == "X":
            x_count += 1
        elif board[i][i] == "0":
            o_count += 1
        elif board[i][i] == ".":
            try:
                empty = (i, i)
            except ValueError:
                pass
        if board[i][2-i] == "X":
            x_count2 += 1
        elif board[i][2-i] == "0":
            o_count2 += 1
        elif board[i][2-i] == ".":
            try:
                empty2 = (i, 2-i)
            except ValueError:
                pass          
    try:
        if x_count == 2 or o_count == 2:
            return True, empty
        elif x_count2 == 2 or o_count2 == 2:
            return True, empty2
    except UnboundLocalError:
            return False, None
    else:
        return False, None



def get_smart_ai_move(board):
    """Returns the coordinates of a valid move for player on board."""
    if is_full(board):
        return None
    else:
        ai_row = smart_ai_rows(board)
        ai_col = smart_ai_cols(board)
        ai_diag = smart_ai_diag(board)
        if ai_row[0] == True:
            if ai_row[1] == ".":
                return ai_row[1]
        elif ai_col[0] == True:
            if ai_col[1] == '.':
                return ai_col[1]
        elif ai_diag[0] == True:
            if ai_diag[1] == ".":
                return ai_diag[1]
        while True:
            random_row = random.randint(0,2)
            random_col = random.randint(0,2)
            if board[random_row][random_col] == '.':
                row_and_col = (random_row, random_col)
                print(f" AI's move: {random_row + 1}, {random_col + 1}")
                return row_and_col
        
            

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
            print("\n Those coordinates are occupied, please choose an empty one.")
            return player
            


def aimark(board, row, col, player):
    if player % 2 == 0:
        board[row][col] = 'X'
    else:
        board[row][col] = '0'
    player += 1
    return player
    


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
    if x_count == 3 or o_count == 3 or x_count2 == 3 or o_count2 == 3:
        return True
    else:
        return False


def has_won(board, active_player):
    """Returns True if player has won the game."""
    return rows(board) or cols(board) or diagonals(board)


def is_full(board):
    """Returns True if board is full."""
    if '.' not in board[0] and '.' not in board[1] and '.' not in board[2]:
        return True
    else:
        return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    print(f'''
   1   2   3 
A  {board[0][0]} | {board[0][1]} | {board[0][2]}
  ---+---+---
B  {board[1][0]} | {board[1][1]} | {board[1][2]}
  ---+---+---
C  {board[2][0]} | {board[2][1]} | {board[2][2]}''')
 


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == 0:
        print("\n It's a tie! \n")
        exit()
    elif winner % 2 == 1:
        print(f"\n X has won! \n")
        exit()
    else:
        print(f"\n 0 has won! \n")
        exit()
    


def tictactoe_game(mode):
    board = init_board()
    print_board(board)
    active_player = 0
    if mode == 'HUMAN-HUMAN':
        while not has_won(board, active_player) and not is_full(board):       
            move = get_move(board, 1)
            row = move[0]
            col = move[1]
            active_player = mark(board, active_player, row, col)
            print_board(board)
        if is_full(board) and not has_won(board, active_player):
            winner = 0
        else:
            winner = active_player
        print_result(winner)
    elif mode == 'HUMAN-AI':
        while not has_won(board, active_player) and not is_full(board):
            while active_player % 2 == 0:
                move = get_move(board, 1)
                row = move[0]
                col = move[1]
                active_player = mark(board, active_player, row, col)
            if is_full(board) and not has_won(board, active_player):
                print_board(board)
                winner = 0
                print_result(winner)
            elif is_full(board) and has_won(board, active_player):
                print_board(board)
                winner = active_player
                print_result(winner)
            else:    
                print_board(board)          
                winner = active_player + 1   
            ai_move = get_ai_move(board)
            ai_row = ai_move[0]
            ai_col = ai_move[1]
            active_player = aimark(board, ai_row, ai_col, active_player)
            print_board(board)
        if is_full(board) and not has_won(board, active_player):
            winner = 0
        else:
            winner = active_player + 1
        print_result(winner)
    elif mode == 'AI-AI':
        while not has_won(board, active_player) and not is_full(board):           
            ai_move = get_ai_move(board)
            ai_row = ai_move[0]
            ai_col = ai_move[1]
            active_player = aimark(board, ai_row, ai_col, active_player)
            print_board(board)
        if is_full(board) and not has_won(board, active_player):
            winner = 0
        else:
            winner = active_player 
        print_result(winner)
    elif mode == "HUMAN-SMART_AI":
        while not has_won(board, active_player) and not is_full(board):
            while active_player % 2 == 0:
                move = get_move(board, 1)
                row = move[0]
                col = move[1]
                active_player = mark(board, active_player, row, col)
            if is_full(board) and not has_won(board, active_player):
                print_board(board)
                winner = 0
                print_result(winner)
            elif is_full(board) and has_won(board, active_player):
                print_board(board)
                winner = active_player
                print_result(winner)
            else:    
                print_board(board)          
                winner = active_player + 1   
            ai_move = get_smart_ai_move(board)
            ai_row = ai_move[0]
            ai_col = ai_move[1]
            active_player = aimark(board, ai_row, ai_col, active_player)
            print_board(board)
        if is_full(board) and not has_won(board, active_player):
            winner = 0
        else:
            winner = active_player + 1
        print_result(winner)
        
def main_menu():
    mode = input('''How do you want to play?
    - 1 single player
    - 2 multiplayer
    - 3 AI against AI
    - 4 single player against smarter AI 
    ''')
    if mode == "1":
        tictactoe_game('HUMAN-AI')
    elif mode == "2":
        tictactoe_game('HUMAN-HUMAN')
    elif mode == "3":
        tictactoe_game('AI-AI')
    elif mode == "4":
        tictactoe_game('HUMAN-SMART_AI')
    return mode


if __name__ == '__main__':
    main_menu()
