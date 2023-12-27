import os

game_board = [[" "," "," "],[" "," "," "],[" "," "," "]]

# Function to print the current state of the board
def print_board():
    print(" {} | {} | {} ".format(game_board[0][0],game_board[0][1],game_board[0][2]))
    print(" {} | {} | {} ".format(game_board[1][0],game_board[1][1],game_board[1][2]))
    print(" {} | {} | {} ".format(game_board[2][0],game_board[2][1],game_board[2][2]))


# Function that prints the introduction page on code launch, will flow to an example of the win condition and board/input layout.
def print_intro():
    os.system('cls')
    print("Welcome To Naughts and Crosses!\n")
    print("The rules are as follows:")
    print("    1. The Naught player will always start the game.")
    print("    2. The game ends after one player is able to place three of their markers in a row, or if all places on the board are filled.")
    input("Please press enter/return to continue:")
    print("\nThe board layout is as follows:\n")
    print_layout()
    print("\nPlayers will select the number that corresponds with the location on the board they wish to place their marker.")


# Function to print the layout of the board. What number each space is mapped to.
def print_layout():
    print(" {} | {} | {} ".format(1,2,3))
    print(" {} | {} | {} ".format(4,5,6))
    print(" {} | {} | {} ".format(7,8,9))

print_intro()