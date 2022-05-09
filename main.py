from tkinter import *

from viewMenu import ActorMenu
from viewJogo import ActorPlayer

class main(Tk):
  def __init__(self, *args, **kwargs):
    Tk.__init__(self, *args, **kwargs)

    container = Frame(self) 
    container.pack(side = "top", fill = "both", expand = True)
    container.grid_rowconfigure(0, weight = 1)
    container.grid_columnconfigure(0, weight = 1)
  
    self.frames = {} 
    for F in (ActorMenu, ActorPlayer):
      frame = F(container, self)
      self.frames[F] = frame
      frame.grid(column=0, row=0, sticky=(N, S, E, W))
    self.show_frame(ActorMenu)
  
  def show_frame(self, cont):
    frame = self.frames[cont]
    frame.tkraise()
    frame.open()

app = main()
app.mainloop()