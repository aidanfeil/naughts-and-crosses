import os

# Function that prints the introduction page on code launch, will flow to an example of the win condition and board/input layout.
def print_intro():
    os.system('cls')
    print("Welcome To Naughts and Crosses!\n\n")
    print("The rules are as follows:")
    print("    1. The Naught player will always start the game.")
    print("    2. The game ends after one player obtains three of their markers in a row.")

print_intro()