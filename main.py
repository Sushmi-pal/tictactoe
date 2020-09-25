import sys
board=["-", "-", "-",
       "-", "-", "-",
       "-", "-", "-"]
current_player="X"
winner=None
game_still_running=True
def display_board():
    print(board[0]+" | " + board[1] + " | " +board[2])
    print(board[3]+" | " + board[4] + " | " +board[5])
    print(board[6]+" | " + board[7] + " | " +board[8])



def check_if_tie():
    global game_still_running
    if '-' not in board:
        game_still_running=False

def flip_player():
    global current_player
    if current_player=='X':
        current_player='O'
    elif current_player=='O':
        current_player='X'

    return current_player

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_row():
    global game_still_running
    row1=board[0]==board[1]==board[2] != "-"
    row2=board[3]==board[4]==board[5] != "-"
    row3=board[6]==board[7]==board[8] != "-"
    if row1 or row2 or row3:
        game_still_running=False

    if row1:
        return board[0]

    elif row2:
        return board[3]

    elif row3:
        return board[6]

def check_column():
    global game_still_running
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
        game_still_running = False

    if col1:
        return board[0]

    elif col2:
        return board[1]

    elif col3:
        return board[2]





def check_if_win():
    global winner

    row_winner =check_row()
    column_winner=check_column()
    diagonal_winner=check_diagonal()

    if row_winner:
        winner=row_winner

    elif column_winner:
        winner=column_winner

    elif diagonal_winner:
        winner=diagonal_winner

    else:
        winner=None
    return

def check_diagonal():
    global game_still_running
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"

    if diag1 or diag2:
        game_still_running = False

    if diag1:
        return board[0]

    elif diag2:
        return board[2]

def handle_turn(player):
    position=int(input('Enter a number from 1 to 9: '))-1
    if '-'  in board[position]:
        board[position]=player

    else:
        print('It is already filled. Next try')
        flip_player()

    display_board()


def play_game():
    display_board()
    while game_still_running:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner=="X" or winner=="O":
        print(winner + " won ")
    else:
        print("Tie")

print('Tic Tac Toe')
inpp =int(input('Enter 1 to play game'+'\n'+ 'Enter 2 to quit'))
if inpp==1:
    play_game()
else:
    sys.exit()

