import sys
import time
import math

import tkinter

import mancala
import ai


def main_gui():

    root = tkinter.Tk()
    root.title("Mancala")

    size = w_width, w_height = 800, 600
    speed = [2, 2]
    white = '#FFFFFF'

    board = mancala.init_board(mancala.BOARD_SIZE)

    canvas = tkinter.Canvas(root, height = w_height, width = w_width)
    canvas.pack()
    
    # photo1 = tkinter.PhotoImage(file = "0380.png")
    # tkinter.Label(root, image = photo1, bg = 'black').pack()


    frame = tkinter.Frame(root, bg = white)
    frame.place(relwidth = 1, relheight = 1)

    root.mainloop()


main_gui()