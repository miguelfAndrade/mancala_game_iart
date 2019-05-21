import time
import sys
import math

# macro for the board size
BOARD_SIZE = 14

PL_1_STORE = 6  # macro for the deposit position for player 1
PL_2_STORE = 13 # macro for the deposit position for player 2


# Variable that stores the opposite position of the current player position
# This is usefull for the eating procedure in the game
# If the last seed of a player is in the position 3, he can now eat the opponent seeds in position 9
opposite = {
    0 : 12,
    1 : 11,
    2 : 10,
    3 : 9,
    4 : 8,
    5 : 7,
    7 : 5,
    8 : 4,
    9 : 3,
    10 : 2,
    11 : 1,
    12 : 0,
}


# Initiate the board for the given size
def init_board(size):
    board = [0] * size
    # for i in range(size):
    #     board[i] = i
    for i in range(size):
        if(i != PL_1_STORE and i != (PL_2_STORE)):
            board[i] = 4
   
# Block Commented for testing
# begin
    # board[0] = 4
    # board[1] = 0
    # board[2] = 0
    # board[3] = 11
    # board[4] = 4
    # board[5] = 3
    # board[6] = 4
    # board[7] = 0
    # board[8] = 6
    # board[9] = 5
    # board[10] = 2
    # board[11] = 0
    # board[12] = 0
    # board[13] = 9
# end

    return board


# Verifies if the board is in a final state, wich means the game is over
def game_over(board):
    count1 = 0
    count2 = 0
    for i in range(len(board)):
        if(i >= 0 and i < PL_1_STORE):
            if(board[i] == 0):
                count1 += 1
        if(i > PL_1_STORE and i < PL_2_STORE):
            if(board[i] == 0):
                count2 += 1

    if(count1 == 6):
        for i in range(7,13):
            board[PL_2_STORE] += board[i]
        return True
    elif(count2 == 6):
        for i in range(0,PL_1_STORE):
            board[PL_1_STORE] += board[i]
        return True
    else:
        return False


# Return the winning player
def player_win(board):
    if(board[PL_1_STORE] > board[PL_2_STORE]):
        return 1
    elif(board[PL_1_STORE] < board[PL_2_STORE]):
        return 2
    else:
        return 0    
    
# Parses the user input to use in the index board
def parse_input(inpt):
    if(inpt > 0 and inpt <= PL_1_STORE):
        return inpt - 1
    elif(inpt > PL_1_STORE and inpt < PL_2_STORE):
        return inpt
    else:
        return

# Handles the logic for the case of a player eats the seeds of the opponent
def eat_seeds(pos, player, board):
    global opposite

    if(player == 0):
        if(board[opposite[pos]] != 0):
            board[PL_1_STORE] += (board[pos]+board[opposite[pos]])
            board[pos] = 0
            board[opposite[pos]] = 0

    if(player == 1):
        if(board[opposite[pos]] != 0):
            board[PL_2_STORE] += (board[pos]+board[opposite[pos]])
            board[pos] = 0
            board[opposite[pos]] = 0


# Handles the logic for moving pieces in the board
def move_piece(pos, player, board):
    i = 0
    if(player == 0):
        hand = board[pos]
        board[pos] = 0
        i = pos+1
        while(hand > 0):
            if(i == PL_2_STORE):
                i = 0
            if(hand == 1 and board[i] == 0 and (i >= 0 and i < PL_1_STORE)):
                board[i] += 1
                eat_seeds(i, player, board)
                hand -= 1
            elif(hand == 1 and i == PL_1_STORE):
                board[i] += 1
                return player
            else:
                board[i] += 1
                hand -= 1
                i += 1

    if(player == 1):
        hand = board[pos]
        board[pos] = 0
        i = pos+1
        while(hand > 0):
            if(i == PL_1_STORE):
                i += 1
            if(i > PL_2_STORE):
                i = 0
            if(hand == 1 and board[i] == 0 and (i > PL_1_STORE and i < PL_2_STORE)):
                board[i] += 1
                eat_seeds(i, player, board)
                hand -= 1
            elif(hand == 1 and i == PL_2_STORE):
                board[i] += 1
                return player
            else:
                board[i] += 1
                hand -= 1
                i += 1

    player += 1
    player = player % 2
    return player



# Verifies if the user input move is valid
def verify_move(pos, player, board):
    if(pos == None):
        print_board_cmd_line(board)
        print("INVALID INPUT!!")
        return False
    if(player == 0):
        if(pos < 0 or pos > 6):
            print_board_cmd_line(board)
            print("You must choose between 1 - 6")
            return False
        if(board[pos] == 0):
            print_board_cmd_line(board)
            print("Empty house, choose another!")
            return False

    elif(player == 1):
        if(pos < 7 or pos > 12):
            print_board_cmd_line(board)
            print("You must choose between 7 - 12")
            return False
        if(board[pos] == 0):
            print_board_cmd_line(board)
            print("Empty house, choose another!")
            return False
    
    return True


# Print to the screen the board
def print_board_cmd_line(board):
    print("\n------12----11----10----09----08----07-----")
    st = "|  |"
    i = 0
    j = 0
    w = len(board)-1
    while(w > 6):
        if(w != (len(board)-1)):  
            if(board[w] > 9):
                st += " |" + str(board[w]) + "| "
            else:
                st += " |0" + str(board[w]) + "| "
        w -= 1
   
    if(board[(len(board)-1)] > 9):
        st += "|  |\n|" + str(board[(len(board)-1)]) + "|"
    else:
        st += "|  |\n|0" + str(board[(len(board)-1)]) + "|"
    while(j < 6):
        st += "      "
        j += 1
    if(board[6] > 9):
        st += "|" + str(board[6]) + "|\n|  |"
    else:
        st += "|0" + str(board[6]) + "|\n|  |"

    while(i < 7):
        if(i != 6):
            if(board[i] > 9):
                st += " |" + str(board[i]) + "| "
            else:
                st += " |0" + str(board[i]) + "| "
        i += 1
    st += "|  |"
    print(st)
    print("------01----02----03----04----05----06-----\n")

