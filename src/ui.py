import sys
import time
import math

import pygame

import mancala
import ai


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