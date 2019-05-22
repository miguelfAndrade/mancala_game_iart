import sys
import time
import math
import random

import mancala


# generates a random number from the available positions
def random_number_gen(board, player):
    valid_moves = playable_pos_list(board, player)
    pos = random.choices(valid_moves)[0]
    return pos

# retrives the available positions for the player
def playable_pos_list(board, player):
    pos_list = []
    for i in range(len(board)):
        if(player == 0):
            if(i >= 0 and i < mancala.PL_1_STORE):
                if(board[i] != 0):
                    pos_list.append(i)
        elif(player == 1):
            if(i > mancala.PL_1_STORE and i < mancala.PL_2_STORE):
                if(board[i] != 0):
                    pos_list.append(i)
    return pos_list


# evaluates how good is the move based in the number of seeds in the player deposit comparing with:
# the oponent deposit
# last move
# not a very good heuristic
def heuristic_2(board, old_board, player):
    score = 0
    if(player == 1):
        if(board[mancala.PL_1_STORE] > old_board[mancala.PL_1_STORE]):
            score += 12
        if(board[mancala.PL_1_STORE] > board[mancala.PL_2_STORE]):
            score += 10
        if(board[mancala.PL_1_STORE] < board[mancala.PL_2_STORE]):
            score -= 8
        else:
            score += 0
    if(player == 0):
        if(board[mancala.PL_2_STORE] > old_board[mancala.PL_2_STORE]):
            score += 12
        if(board[mancala.PL_2_STORE] > board[mancala.PL_1_STORE]):
            score += 10
        if(board[mancala.PL_2_STORE] < board[mancala.PL_1_STORE]):
            score -= 8
        else:
            score += 0
    
    return score

# evaluates how good is the move based in the number of seeds in the player deposit
def heuristic(board, player):
    if(player == 0):
        return (board[mancala.PL_1_STORE] - board[mancala.PL_2_STORE])
    if(player == 1):
        return (board[mancala.PL_2_STORE] - board[mancala.PL_1_STORE])

#Utility function
def utility_function(board, player):
    if(player == 0):
        if(mancala.player_win(board) == 1):
            return (None, 100000000000000)
        elif(mancala.player_win(board) == 2):
            return (None, -100000000000000)
        else:
            return (None, 0)
    if(player == 1):
        if(mancala.player_win(board) == 2):
            return (None, 100000000000000)
        elif(mancala.player_win(board) == 1):
            return (None, -100000000000000)
        else:
            return (None, 0)

# picks the best move based on the score calculated with the heuristic_2 function
def pick_best_pos(board, player):
    valid_locations = playable_pos_list(board, player)
    best_score = -1000000
    best_pos = random.choice(valid_locations)
    for pos in valid_locations:
        # print("POS: " + str(pos))
        temp_board = board.copy()
        pl_temp = mancala.move_piece(pos, player, temp_board)
        score = heuristic_2(temp_board, board, player)
        # score = heuristic(temp_board, player)
        # print("SCORE: " + str(score))
        # print("BEST SCORE: " + str(best_score))
        if(score > best_score):
            best_score = score
            best_pos = pos
    
    return best_pos, best_score



# function minimax(node, depth, maximizingPlayer) is
#     if depth = 0 or node is a terminal node then
#         return the heuristic value of node
#     if maximizingPlayer then
#         value := −∞
#         for each child of node do
#             value := max(value, minimax(child, depth − 1, FALSE))
#         return value
#     else (* minimizing player *)
#         value := +∞
#         for each child of node do
#             value := min(value, minimax(child, depth − 1, TRUE))
#         return value
# (* Initial call *)
# minimax(origin, depth, TRUE)

# return true if it is a terminal node and false if it is not
def terminal_node(board):
    return mancala.game_over(board)

# minimax algorithm based on the above commented pseudocode
def minimax(board, old_board, depth, maximizingPlayer, player):
    valid_locations = playable_pos_list(board, player)
    is_terminal = terminal_node(board)

    if (depth == 0 or is_terminal):
        if(is_terminal):
            return utility_function(board, player)
        else:
            # value = heuristic(board, player)
            value = pick_best_pos(board, player)[1]
            return (None, value)

    if(maximizingPlayer):
        value = -math.inf
        best_pos = random.choice(valid_locations)
        for pos in valid_locations:
            b_copy = board.copy()
            player_tmp = mancala.move_piece(pos, player, b_copy)
            if(player_tmp == player):
                new_score = minimax(b_copy, board, depth-1, True, player_tmp)[1]
            else:
                new_score = minimax(b_copy, board, depth-1, False, player_tmp)[1]
            if(new_score > value):
                value = new_score
                best_pos = pos
        return (best_pos, value)
    else:
        value = math.inf
        best_pos = random.choice(valid_locations)
        for pos in valid_locations:
            b_copy = board.copy()
            player_tmp = mancala.move_piece(pos, player, b_copy)
            if(player_tmp != player):
                new_score = minimax(b_copy, board, depth-1, True, player_tmp)[1]
            else:
                new_score = minimax(b_copy, board, depth-1, False, player_tmp)[1]
            if(new_score < value):
                value = new_score
                best_pos = pos
        return (best_pos, value)


# function alphabeta(node, depth, α, β, maximizingPlayer) is
#     if depth = 0 or node is a terminal node then
#         return the heuristic value of node
#     if maximizingPlayer then
#         value := −∞
#         for each child of node do
#             value := max(value, alphabeta(child, depth − 1, α, β, FALSE))
#             α := max(α, value)
#             if α ≥ β then
#                 break (* β cut-off *)
#         return value
#     else
#         value := +∞
#         for each child of node do
#             value := min(value, alphabeta(child, depth − 1, α, β, TRUE))
#             β := min(β, value)
#             if α ≥ β then
#                 break (* α cut-off *)
#         return value
# (* Initial call *)
# alphabeta(origin, depth, −∞, +∞, TRUE)

# minimax algorithm with alpha beta pruning based on the above commented pseudocode
def minimax_alpha_beta(board, old_board, depth, alpha, beta, maximizingPlayer, player):
    valid_locations = playable_pos_list(board, player)
    is_terminal = terminal_node(board)

    if (depth == 0 or is_terminal):
        if(is_terminal):
            return utility_function(board, player)
        else:
            value = heuristic(board, player)
            # value = pick_best_pos(board, player)[1]
            return (None, value)

    if(maximizingPlayer):
        value = -math.inf
        best_pos = random.choice(valid_locations)
        for pos in valid_locations:
            b_copy = board.copy()
            player_tmp = mancala.move_piece(pos, player, b_copy)
            if(player_tmp == player):
                new_score = minimax_alpha_beta(b_copy, board, depth-1, alpha, beta, True, player_tmp)[1]
            else:
                new_score = minimax_alpha_beta(b_copy, board, depth-1, alpha, beta, False, player_tmp)[1]
            if(new_score > value):
                value = new_score
                best_pos = pos
            alpha = max(alpha, value)
            if(alpha >= beta):
                break
        return (best_pos, value)
    else:
        value = math.inf
        best_pos = random.choice(valid_locations)
        for pos in valid_locations:
            b_copy = board.copy()
            player_tmp = mancala.move_piece(pos, player, b_copy)
            if(player_tmp != player):
                new_score = minimax_alpha_beta(b_copy, board, depth-1, alpha, beta, True, player_tmp)[1]
            else:
                new_score = minimax_alpha_beta(b_copy, board, depth-1, alpha, beta, False, player_tmp)[1]
            if(new_score < value):
                value = new_score
                best_pos = pos
            beta = min(beta, value)
            if(alpha >= beta):
                break
        return (best_pos, value)

