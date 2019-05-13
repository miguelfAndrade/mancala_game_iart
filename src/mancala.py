import time

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

def init_board(size):
    board = [0] * size
    # for i in range(size):
    #     board[i] = i
    for i in range(size):
        if(i != 6 and i != (size-1)):
            board[i] = 4
   
    # for i in range(size):
    #     if(i >= 7 and i < 13):
    #         board[i] = 0
   
    # board[6] = 20
    # board[11] = 0
    # board[12] = 0

    return board


def game_over(board):
    count1 = 0
    count2 = 0
    for i in range(len(board)):
        if(i >= 0 and i < 6):
            if(board[i] == 0):
                count1 += 1
        if(i > 6 and i < 13):
            if(board[i] == 0):
                count2 += 1

    if(count1 == 6):
        for i in range(6,13):
            board[13] += board[i]
        return True
    elif(count2 == 6):
        for i in range(0,6):
            board[6] += board[i]
        return True
    else:
        return False



def player_win(n_seed_pl_1, n_seed_pl_2):
    if(n_seed_pl_1 > n_seed_pl_2):
        return 1
    elif(n_seed_pl_1 < n_seed_pl_2):
        return 2
    else:
        return 0    
    

def parse_input(inpt):
    if(inpt > 0 and inpt < 7):
        return inpt - 1
    elif(inpt > 6 and inpt < 13):
        return inpt
    else:
        return

def eat_seeds(pos, player, board):
    global opposite

    if(player == 0):
        if(board[opposite[pos]] != 0):
            board[6] += (board[pos]+board[opposite[pos]])
            board[pos] = 0
            board[opposite[pos]] = 0

    if(player == 1):
        if(board[opposite[pos]] != 0):
            board[13] += (board[pos]+board[opposite[pos]])
            board[pos] = 0
            board[opposite[pos]] = 0


def move_piece(pos, player, board):
    i = 0
    if(player == 0):
        hand = board[pos]
        board[pos] = 0
        i = pos+1
        while(hand > 0):
            if(i == 13):
                i = 0
            if(hand == 1 and board[i] == 0 and (i >= 0 and i < 6)):
                board[i] += 1
                eat_seeds(i, player, board)
                hand -= 1
            elif(hand == 1 and i == 6):
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
            if(i == 6):
                i += 1
            if(i > 13):
                i = 0
            if(hand == 1 and board[i] == 0 and (i > 6 and i < 13)):
                board[i] += 1
                eat_seeds(i, player, board)
                hand -= 1
            elif(hand == 1 and i == 13):
                board[i] += 1
                return player
            else:
                board[i] += 1
                hand -= 1
                i += 1

    player += 1
    player = player % 2
    return player




def verify_move(pos, player, board):
    if(pos == None):
        print_board_cmd_line(board)
        print("Invalid Input!!")
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



def main():
    board = init_board(14)
    print_board_cmd_line(board)
    player = 0
    winner = 0
    while(not game_over(board)):
        print("Player " + str(player + 1) + " turn!")
        piece = parse_input(int(input("Choose your Piece: ")))
        print(piece)
        if(not verify_move(piece, player, board)):
            continue
        player = move_piece(piece,player,board)
        time.sleep(1)
        print_board_cmd_line(board)
    
    winner = player_win(board[6], board[13])
    print("GAME OVER")
    print("Number of seeds:")
    print("Player 1: " + str(board[6]))
    print("Player 2: " + str(board[13]))
    if(winner != 0):
        print("Player " + str(winner) + " won the game!!!")
    else:
        print("It's a draw!!")


main()


