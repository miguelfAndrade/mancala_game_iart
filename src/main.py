import sys
import time
import math

import pygame

import mancala
import ai


def player_vs_player(board):
    mancala.print_board_cmd_line(board)
    player = 0
    winner = 0
    while(not mancala.game_over(board)):
        print("Player " + str(player + 1) + " turn!")
        teste = ai.playable_pos_list(board, player)
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
    
    winner = mancala.player_win(board)
    print("GAME OVER")
    print("Number of seeds:")
    print("Player 1: " + str(board[mancala.PL_1_STORE]))
    print("Player 2: " + str(board[mancala.PL_2_STORE]))
    if(winner != 0):
        print("Player " + str(winner) + " won the game!!!")
    else:
        print("It's a draw!!")



def player_vs_pc(board, level):
    mancala.print_board_cmd_line(board)
    player = 0
    winner = 0
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
            piece, minimax_score = ai.minimax_alpha_beta(board, None, level, -math.inf, math.inf, True, player)
            print("CHOOSEN POS: " + str(piece))
            if(not mancala.verify_move(piece, player, board)):
                continue
            player = mancala.move_piece(piece, player, board)
            mancala.print_board_cmd_line(board)
            time.sleep(1)

    
    winner = mancala.player_win(board)
    print("GAME OVER")
    print("Number of seeds:")
    print("Player 1: " + str(board[mancala.PL_1_STORE]))
    print("Player 2: " + str(board[mancala.PL_2_STORE]))
    if(winner != 0):
        print("Player " + str(winner) + " won the game!!!")
    else:
        print("It's a draw!!")


def pc_vs_pc(board, level1, level2):
    mancala.print_board_cmd_line(board)
    player = 0
    winner = 0
    while(not mancala.game_over(board)):
        if(player == 0):
            print("Player 1 turn!")
            print(player)
            piece, minimax_score = ai.minimax_alpha_beta(board, None, level1, -math.inf, math.inf, True, player)
            print("Player 1 choose: " + str(piece+1))
            # print("minimax score: " + str(minimax_score))
            if(not mancala.verify_move(piece, player, board)):
                continue
            player = mancala.move_piece(piece, player, board)
            mancala.print_board_cmd_line(board)
        elif(player == 1):
            print("Player 2 turn!")
            piece, minimax_score = ai.minimax_alpha_beta(board, None, level2, -math.inf, math.inf, True, player)
            print("Player 2 choose: " + str(piece))
            # print("minimax score: " + str(minimax_score_2))
            if(not mancala.verify_move(piece, player, board)):
                continue
            player = mancala.move_piece(piece, player, board)
            mancala.print_board_cmd_line(board)
            # time.sleep(1)

    
    winner = mancala.player_win(board)
    print("GAME OVER")
    print("Number of seeds:")
    print("Player 1: " + str(board[mancala.PL_1_STORE]))
    print("Player 2: " + str(board[mancala.PL_2_STORE]))
    if(winner != 0):
        print("Player " + str(winner) + " won the game!!!")
    else:
        print("It's a draw!!")




def main_cmd_line_game():
    print("\n\n\n\n\nChoose your mode:\n")
    print("1 - Player vs Player")
    print("2 - Player vs PC")
    print("3 - PC vs PC")
    while(True):
        try:
            user = int(input("Select: "))
            if(user == 1 or user == 2 or user == 3):
                break
            else:
                print("Choose between 1, 2 and 3!")
                continue
        except Exception:
            print("INVALID INPUT!")
            continue

    board = mancala.init_board(mancala.BOARD_SIZE)
    if(user == 1):
        player_vs_player(board)
    elif(user == 2):
        print("Choose the difficulty level:")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")
        while(True):
            try:
                level = int(input("Select: "))
                if(level == 1 or level == 2 or level == 3):
                    break
                else:
                    print("Choose between 1, 2 and 3!")
                    continue
            except Exception:
                print("INVALID INPUT!")
                continue
        if(level == 1):
            player_vs_pc(board, 2)
        elif(level == 2):
            player_vs_pc(board, 5)
        else:
            player_vs_pc(board, 8)
    else:
        while(True):
            print("Choose the difficulty level for pc 1:")
            print("1 - Easy")
            print("2 - Medium")
            print("3 - Hard")
            try:
                level1 = int(input("Select: "))
                if(level1 == 1 or level1 == 2 or level1 == 3):
                    break
                else:
                    print("Choose between 1, 2 and 3!")
                    continue
            except Exception:
                print("INVALID INPUT!")
                continue

        while(True):
            print("Choose the difficulty level for pc 2:")
            print("1 - Easy")
            print("2 - Medium")
            print("3 - Hard")
            try:
                level2 = int(input("Select: "))
                if(level2 == 1 or level2 == 2 or level2 == 3):
                    break
                else:
                    print("Choose between 1, 2 and 3!")
                    continue
            except Exception:
                print("INVALID INPUT!")
                continue
        
        if(level1 == 1):
            pc_1 = 2
        elif(level1 == 2):
            pc_1 = 5
        else:
            pc_1 = 8

        if(level2 == 1):
            pc_2 = 2
        elif(level2 == 2):
            pc_2 = 5
        else:
            pc_2 = 8
        
        pc_vs_pc(board, pc_1, pc_2)



def choose_cmd_or_gui():
    print("\n\n\nMANCALA BOARD GAME")
    print("\nSelect one of the options:")
    print("1 - Comand line Game")
    print("2 - Graphical Interface Game")
    while(True):
        try:
            user = int(input("Select: "))
            if(user == 1 or user == 2):
                break
            else:
                print("Choose between 1 and 2!")
                continue
        except Exception:
            print("INVALID INPUT!")
            continue
    if(user == 1):
        main_cmd_line_game()
    else:
        main_gui()
        # print("Not implemented!")


def main_gui():

    pygame.init()

    size = width, height = 800, 600
    speed = [2, 2]
    white = (255, 255, 255)

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Mancala")

    board = mancala.init_board(mancala.BOARD_SIZE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Hello!!!!")


choose_cmd_or_gui()