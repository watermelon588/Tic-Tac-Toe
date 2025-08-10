
from IPython.display import clear_output

# Display function to print the current state of the board
def display_board(board):
    clear_output()  # This clears the output in Jupyter so the board updates cleanly
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print('-----------')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('-----------')
    print(f' {board[7]} | {board[8]} | {board[9]} ')



def player_input():

    # output will be in the form of (player_1_marker,player_2_marker)....then we can perform tuple unpacking.

    marker = 'None'
    while marker != 'X' and marker != 'O':
        marker = input("Player1 : Choose (X or O) : ").upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


def place_marker(board, marker, position):
    board[position] = marker
    


def win_check(board, mark):

    winning_combinations = [
        [1,2,3],  # top row
        [4,5,6],  # middle row
        [7,8,9],  #bottom row
        [1,4,7],  #left column
        [2,5,8],  # middle column
        [3,6,9],  #right column
        [1,5,9],  # diagonal 1
        [3,5,7],  #diagonal 2
    ]
    for combinations in winning_combinations:
        if all(board[i] == mark for i in combinations ):
            return True
    return False


import random

def choose_first():
    
    flip = random.randint(0,1)
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    
    return board[position] == ' '


def full_board_check(board):
    
    for places in range(1,10):
        if space_check(board,places):  # calling  up the 'space_check' function to check for the all possible places by itterating through board
            return False               # by using for loop.
    return True


def player_choice(board):
    
    position = 0
    while position not in range(1,10) or not space_check(board,position):
        position = int(input("Choose a position:(1-9) "))
    return position


def replay():
    
    response = input(" Wanna play again? (YES/NO) : ").upper()
    return response == "YES"


# WHILE LOOP TO KEEP RUNNING THE GAME.

print('Welcome to TIC TAC TOE!')
while True:

    # SET UP THE GAME 
    
    ## BOARD > WHO IS FIRST > MARKER CHOICE 
    the_board = [' ' for _ in range(10)]  # 3x3 board
    (player_1_marker,player_2_marker) = player_input()
    Turn = choose_first()
    print(Turn + " goes first !")

    ready_play = input("Are you READY to play ?:(y/n)").lower()
    if ready_play == 'y':
        game_on = True
    else:
        game_on = False
    # GAME PLAY
    while game_on:

        if Turn == "Player 1":

            ## Player 1's turn .
            #1. show the board.
            display_board(the_board)
            #2. choose a position
            position = player_choice(the_board)
            #3. place the marker on the position
            place_marker(the_board,player_1_marker,position)
            #4. check if they won.
            if win_check(the_board,player_1_marker):
                display_board(the_board)
                print(" PLAYER 1 HAS WON !!")
                game_on = False
            #5. or check if it is a tie.
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print(" IT'S A TIE !!")
                    game_on = False
            #6. no tie / win ? next players turn.
                else:
                    Turn = "Player 2"

        else:

            ## Player 2's turn .
            #1. show the board.
            display_board(the_board)
            #2. choose a position
            position = player_choice(the_board)
            #3. place the marker on the position
            place_marker(the_board,player_2_marker,position)
            #4. check if they won.
            if win_check(the_board,player_2_marker):
                display_board(the_board)
                print(" PLAYER 2 HAS WON !!")
                game_on = False
            #5. or check if it is a tie.
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print(" IT'S A TIE !!")
                    game_on = False
            #6. no tie / win ? next players turn.
                else:
                    Turn = "Player 1"
        
        
            
    # BREAK OUT OF THE GAME .
    if not replay():
        break

#x.. THANK YOU :)
