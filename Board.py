import tkinter as tk
import random
from tkinter import ttk

from Constants import *
from GameOfLife import GameOfLife

class GameOfLifeBoard(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=800, height=800, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = NUM_OF_ROWS
        self.columns = NUM_OF_COLUMNS
        self.cellwidth = CELL_WIDTH
        self.cellheight = CELL_HEIGHT

        self.gameState = GAME_STATE_PAUSED

        self.game = GameOfLife()
        board = self.game.getBoard()
        self.rect = {}
        for column in range(self.columns):
            for row in range(self.rows):
                x1 = column * self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                color = "blue"
                if board[row][column] == 1:
                    color = "green"
                self.rect[row, column] = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags=CANVAS_CELL_TAG)

        self.canvas.tag_bind(CANVAS_CELL_TAG, "<Button-1>", self.cellClick)

        self.canvas.create_text(50, 750, text="Start", tags=CANVAS_START_TAG)
        self.canvas.tag_bind(CANVAS_START_TAG, "<Button-1>", self.onClickStart)

        self.canvas.create_text(250, 750, text="Stop", tags=CANVAS_STOP_TAG)
        self.canvas.tag_bind(CANVAS_STOP_TAG, "<Button-1>", self.onClickStop)


    def redraw(self):
        board = self.game.getBoard()
        self.canvas.itemconfig(CANVAS_CELL_TAG, fill="blue")
        for row in range(self.rows):
            for column in range(self.columns):
                if board[row][column] == 1:
                    item_id = self.rect[row, column]
                    self.canvas.itemconfig(item_id, fill="green")

    def playGame(self):
        if self.gameState == GAME_STATE_PLAYING:
            board = self.game.updateToNextStep()
            self.redraw()
            self.after(STEP_DELAY, lambda: self.playGame())

    def cellClick(self, event):
        x = event.x
        y = event.y
        row = int(y/CELL_HEIGHT)
        column = int(x/CELL_WIDTH)
        self.game.changeCellState(row, column)

        color = "blue"
        if self.game.Board[row][column] == 1:
            color = "green"

        item_id = self.rect[row, column]
        self.canvas.itemconfig(item_id, fill=color)

    def onClickStart(self, *args):
        self.gameState = GAME_STATE_PLAYING
        self.playGame()

    def onClickStop(self, *args):
        self.gameState = GAME_STATE_PAUSED

