#Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.

from IPython.display import clear_output

# Display function to print the current state of the board
def display_board(board):
    clear_output()  # This clears the output in Jupyter so the board updates cleanly
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print('-----------')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('-----------')
    print(f' {board[7]} | {board[8]} | {board[9]} ')


#Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.

def player_input():

    # output will be in the form of (player_1_marker,player_2_marker)....then we can perform tuple unpacking.

    marker = 'None'
    while marker != 'X' and marker != 'O':
        marker = input("Player1 : Choose (X or O) : ").upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

#Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    board[position] = marker
    
#Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.

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

#Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.

import random

def choose_first():
    
    flip = random.randint(0,1)
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"

#Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):
    
    return board[position] == ' '

#Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def full_board_check(board):
    
    for places in range(1,10):
        if space_check(board,places):  # calling  up the 'space_check' function to check for the all possible places by itterating through board
            return False               # by using for loop.
    return True

#Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.

def player_choice(board):
    
    position = 0
    while position not in range(1,10) or not space_check(board,position):
        position = int(input("Choose a position:(1-9) "))
    return position

#Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.

def replay():
    
    response = input(" Wanna play again? (YES/NO) : ").upper()
    return response == "YES"

#Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!

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
