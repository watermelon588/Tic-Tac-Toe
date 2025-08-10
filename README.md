🎮 Tic-Tac-Toe (Python Console Version)
A simple two-player Tic-Tac-Toe game built in Python that runs in the terminal/console.
The game follows a number-pad layout for positions and includes interactive input prompts.

📌 Features
Interactive Player vs Player gameplay.

Players choose their marker (X or O).

Randomized first player selection.

Automatic board updates after each turn.

Win & Tie detection logic.

Option to replay the game without restarting the program.

Number Pad Layout for board positions:

markdown
Copy
Edit

 7 | 8 | 9
-----------
 4 | 5 | 6
-----------
 1 | 2 | 3

🛠️ Requirements
Python 3.x

IPython package (for clear_output() in Jupyter Notebooks)
Install via:

bash
Copy
Edit
pip install ipython
🚀 How to Run
Clone or Download the script.

Make sure Python is installed on your system.

Run the script:

bash
Copy
Edit
python tic_tac_toe.py
🎯 How to Play
Choose your marker (X or O) when prompted.

The game will randomly decide who plays first.

Enter a number (1-9) to place your marker on the board.

The first player to get three in a row (horizontally, vertically, or diagonally) wins.

If the board fills without a winner, the game ends in a tie.

After the game ends, you can choose to play again.

📂 Code Structure
Function	Purpose
display_board()	Prints the current board state.
player_input()	Lets Player 1 choose X or O.
place_marker()	Places a marker at a chosen position.
win_check()	Checks if a player has won.
choose_first()	Randomly selects which player goes first.
space_check()	Checks if a position is available.
full_board_check()	Checks if the board is full (tie).
player_choice()	Gets a valid position from the player.
replay()	Asks players if they want to play again.


EXAMPLE  GAME PLAY 


Welcome to TIC TAC TOE!
Player 1: Choose (X or O): X
Player 1 goes first!
Are you READY to play? (y/n) y

 X | - | -
-----------
 - | - | -
-----------
 - | - | -

Choose a position (1-9): 5
...
