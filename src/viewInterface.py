from tkinter import *

from viewMenu import MainMenu
from viewJogo import Game

class InterfaceJogador(Tk):
  def __init__(self, *args, **kwargs):
    Tk.__init__(self, *args, **kwargs)

    container = Frame(self) 
    container.pack(side = "top", fill = "both", expand = True)
    container.grid_rowconfigure(0, weight = 1)
    container.grid_columnconfigure(0, weight = 1)

    self.game = Game(container, self)
    self.game.grid(column=0, row=0, sticky=(N, S, E, W))

    self.main_menu = MainMenu(container, self)
    self.main_menu.grid(column=0, row=0, sticky=(N, S, E, W))
    self.main_menu.tkraise()
    self.main_menu.open()