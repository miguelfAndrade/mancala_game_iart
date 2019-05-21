import sys
import math
import time

import mancala
import ai



def player_vs_pc(board, level):
    mancala.print_board_cmd_line(board)
    player = 0
    winner = 0
    moves = []
    while(not mancala.game_over(board)):
        if(player == 0):
            print("Player " + str(player + 1) + " turn!")
            try:
                piece = mancala.parse_input(int(input("Choose your Piece: ")))
            except Exception:
                mancala.print_board_cmd_line(board)
                print("INVALID INPUT!!")
                continue
            if(not mancala.verify_move(piece, player, board)):
                continue
            player = mancala.move_piece(piece, player, board)
            mancala.print_board_cmd_line(board)
        elif(player == 1):
            print("Player " + str(player + 1) + " turn!")
            tic = time.clock()
            piece, minimax_score = ai.minimax_alpha_beta(board, None, level, -math.inf, math.inf, True, player)
            toc = time.clock()
            print("CHOOSEN POS: " + str(piece))
            print("Processing Time: " + str(toc-tic))
            if(not mancala.verify_move(piece, player, board)):
                continue
            player = mancala.move_piece(piece, player, board)
            moves.append(piece)
            mancala.print_board_cmd_line(board)
            time.sleep(1)

    
    winner = mancala.player_win(board)
    print("GAME OVER")
    print("Number of seeds:")
    print("Player 1: " + str(board[mancala.PL_1_STORE]))
    print("Player 2: " + str(board[mancala.PL_2_STORE]) + " | Moves Done: " + str(moves))
    if(winner != 0):
        print("Player " + str(winner) + " won the game!!!")
    else:
        print("It's a draw!!")


def pc_vs_pc(board, level1, level2):
    mancala.print_board_cmd_line(board)
    player = 0
    winner = 0
    moves_1 = []
    moves_2 = []
    while(not mancala.game_over(board)):
        if(player == 0):
            print("Player 1 turn!")
            print(player)
            tic1 = time.clock()
            piece, minimax_score = ai.minimax_alpha_beta(board, None, level1, -math.inf, math.inf, True, player)
            toc1 = time.clock()
            print("Player 1 choose: " + str(piece+1))
            print("Processing Time For Player 1: " + str(toc1-tic1))
            if(not mancala.verify_move(piece, player, board)):
                continue
            player = mancala.move_piece(piece, player, board)
            moves_1.append(piece)
            mancala.print_board_cmd_line(board)
        elif(player == 1):
            print("Player 2 turn!")
            tic2 = time.clock()
            piece, minimax_score = ai.minimax_alpha_beta(board, None, level2, -math.inf, math.inf, True, player)
            toc2 = time.clock()
            print("Player 2 choose: " + str(piece))
            print("Processing Time For Player 2: " + str(toc2-tic2))
            if(not mancala.verify_move(piece, player, board)):
                continue
            player = mancala.move_piece(piece, player, board)
            moves_2.append(piece)
            mancala.print_board_cmd_line(board)

    
    winner = mancala.player_win(board)
    print("GAME OVER")
    print("Number of seeds:")
    print("Player 1: " + str(board[mancala.PL_1_STORE]) + " | Moves Done: " + str(moves_1))
    print("Player 2: " + str(board[mancala.PL_2_STORE]) + " | Moves Done: " + str(moves_2))
    if(winner != 0):
        print("Player " + str(winner) + " won the game!!!")
    else:
        print("It's a draw!!")


board = mancala.init_board(mancala.BOARD_SIZE)
# player_vs_pc(board, 2)
pc_vs_pc(board, 7, 2)

