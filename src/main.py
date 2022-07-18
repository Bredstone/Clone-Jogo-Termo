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
  
    self.frames = {} 
    for F in (MainMenu, Game):
      frame = F(container, self)
      self.frames[F] = frame
      frame.grid(column=0, row=0, sticky=(N, S, E, W))
    self.show_frame(MainMenu)
  
  def show_frame(self, cont):
    frame = self.frames[cont]
    frame.tkraise()
    frame.open()

if __name__ == '__main__':
  app = InterfaceJogador()
  app.mainloop()