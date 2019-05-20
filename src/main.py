import sys
import time

import pygame

import mancala
import ai


def player_vs_player(board):
    mancala.print_board_cmd_line(board)
    player = 0
    winner = 0
    teste = []
    while(not mancala.game_over(board)):
        print("Player " + str(player + 1) + " turn!")
        teste = ai.playable_pos_list(board, player)
        print("BEST POS: " + str(ai.pick_best_pos(board, player)))
        print(teste)
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



def player_vs_pc(board):
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
            # piece = ai.random_number_gen(7,12)
            # piece = ai.pick_best_pos(board, player)
            piece, minimax_score = ai.minimax(board, board, 1, True, player)
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


def pc_vs_pc(board):
    mancala.print_board_cmd_line(board)
    player = 0
    winner = 0
    while(not mancala.game_over(board)):
        if(player == 0):
            print("Player 1 turn!")
            # piece = ai.random_number_gen(board, player)
            print(player)
            piece, minimax_score = ai.minimax(board, None, 5, True, player)
            print("Player 1 choose: " + str(piece+1))
            # print("minimax score: " + str(minimax_score))
            if(not mancala.verify_move(piece, player, board)):
                continue
            player = mancala.move_piece(piece, player, board)
            mancala.print_board_cmd_line(board)
        elif(player == 1):
            print("Player 2 turn!")
            # piece = ai.random_number_gen(board, player)
            piece, minimax_score_2 = ai.minimax(board, None, 1, True, player)
            print("Player 2 choose: " + str(piece))
            # print("minimax score: " + str(minimax_score_2))
            if(not mancala.verify_move(piece, player, board)):
                continue
            player = mancala.move_piece(piece, player, board)
            mancala.print_board_cmd_line(board)
            # time.sleep(1)

    
    winner = mancala.player_win(board)
    print("minimax 1 score: " + str(minimax_score))
    # print("minimax 2 score: " + str(minimax_score_2))
    print("GAME OVER")
    print("Number of seeds:")
    print("Player 1: " + str(board[mancala.PL_1_STORE]))
    print("Player 2: " + str(board[mancala.PL_2_STORE]))
    if(winner != 0):
        print("Player " + str(winner) + " won the game!!!")
    else:
        print("It's a draw!!")




def main_cmd_line_game():
    board = mancala.init_board(mancala.BOARD_SIZE)
    # player_vs_player(board)
    # player_vs_pc(board)
    pc_vs_pc(board)




def main():

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
                player_vs_player(board)


main_cmd_line_game()