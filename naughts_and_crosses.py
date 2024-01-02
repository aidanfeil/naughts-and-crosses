import os

# Variable Declarations here
game_board = [[" "," "," "],[" "," "," "],[" "," "," "]]
game_turn = 0
player_one = ''
player_two = ''

# Var for continuing game while state = 0
# State integers are (0 = Game active, 1 = Player One win, 2 = Player Two win, 3 = Draw, 4 = Player Exit)
game_state = 0

mapping_dict = {
    "1" : "[0][0]",
    "2" : "[0][1]",
    "3" : "[0][2]",
    "4" : "[1][0]",
    "5" : "[1][1]",
    "6" : "[1][2]",
    "7" : "[2][0]",
    "8" : "[2][1]",
    "9" : "[2][2]",
}

# Function to print the current state of the board with a turn count and indicator of whose turn it is
def print_board(active_player):
    print("Turn: {}    {}'s Turn\n".format(game_turn, active_player))
    print(" {} | {} | {} ".format(game_board[0][0],game_board[0][1],game_board[0][2]))
    print(" {} | {} | {} ".format(game_board[1][0],game_board[1][1],game_board[1][2]))
    print(" {} | {} | {} ".format(game_board[2][0],game_board[2][1],game_board[2][2]))


# Function that prints the introduction page on code launch, will flow to an example of the win condition and board/input layout.
def print_intro():
    global player_one
    global player_two
    os.system('cls')
    print("Welcome To Naughts and Crosses!\n")
    print("The rules are as follows:")
    print("    1. The Naught player will always start the game.")
    print("    2. The game ends after one player is able to place three of their markers in a row, or if all places on the board are filled.")
    print("\nPlayers will select the number that corresponds with the location on the board they wish to place their marker.\n")
    input("Please press enter/return to continue:")

    print("\nThe board layout is as follows:\n")
    print_layout()

    player_one = input("\nPlease enter Player One's name: ")
    player_two = input("Please enter Player Two's name: ")
    print("{} (O) vs {} (X)".format(player_one, player_two))
    input("Press Enter to continue:")


# Function to print the layout of the board. What number each space is mapped to.
def print_layout():
    print(" {} | {} | {} ".format(1,2,3))
    print(" {} | {} | {} ".format(4,5,6))
    print(" {} | {} | {} ".format(7,8,9))

# Function to check if the position the player selected has been filled by either player, or if it remains blank.
def check_position_fill(user_in):
    pos1 = int(mapping_dict[user_in][1])
    pos2 = int(mapping_dict[user_in][4])
    if game_board[pos1][pos2] == 'X' or game_board[pos1][pos2] == 'O':
        return True
    else:
        return False
    
#def check_win():
    
# Function to fill in the spot on the board that the player selected.
def position_fill(user_in, player_val):
    pos1 = int(mapping_dict[user_in][1])
    pos2 = int(mapping_dict[user_in][4])
    game_board[pos1][pos2] = player_val

# Function to check if a user entered 'exit'
def validate_input(user_in):
    data_valid = False
    if user_in.lower() == 'exit':
        return 'exit'
    while data_valid == False:
        while user_in not in mapping_dict:
            user_in = input("That is not a valid option, please enter another number: ")
        if check_position_fill(user_in):
            user_in = input("That position is already filled, please select another position: ")
        else: 
            data_valid = True
    return user_in


# Function for player one's turn
def player_one_turn():
    user_in = input("\nWhere would you like to place your marker?")
    user_in = validate_input(user_in)
    if user_in == 'exit':
        return 'exit'
    position_fill(user_in, 'O')

# Function for player two's turn
def player_two_turn():
    user_in = input("\nWhere would you like to place your marker?")
    user_in = validate_input(user_in)
    if user_in == 'exit':
        return 'exit'
    position_fill(user_in, 'X')

# MAIN CODE BLOCK
# Calls the Intro function to set up the game. 
print_intro()

# While loop to keep the game running turn by turn
while game_state == 0:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    game_turn += 1
    if (game_turn % 2) == 1:
        print_board(player_one)
        if player_one_turn() == 'exit':
            game_state = 4
        if game_state == 4:
            break
    elif (game_turn % 2) == 0:
        print_board(player_two)
        if player_two_turn() == 'exit':
            game_state = 4
        if game_state == 4:
            break