from tkinter import *

from pathResolver import resource_path
from viewJogo import Game

class MainMenu(Frame):
  def __init__(self, parent, controller):
    Frame.__init__(self, parent)
    self.controller = controller
    self.root = self

    # Mainframe
    mainframe = Frame(self.root, width=700, height=500, bg='#6e5c62', padx=120, pady=45)
    mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.rowconfigure(5, weight=1)
    mainframe.grid_propagate(0)

    # Título
    self.title_image = PhotoImage(file=resource_path('./images/title.png'))
    Label(mainframe, image=self.title_image, bg='#6e5c62').grid(row=0, column=0, sticky=(N, E, W))

    # Jogador 1
    self.player1_image = PhotoImage(file=resource_path('./images/player1.png'))
    Label(mainframe, image=self.player1_image, bg='#6e5c62').grid(row=1, column=0, sticky=W)
    
    border_entry1 = Frame(mainframe, bg='#312a2c', padx=3, pady=3)
    border_entry1.grid(row=2, column=0, sticky=(E, W))
    border_entry1.columnconfigure(0, weight=1)
    border_entry1.rowconfigure(0, weight=1)
    
    Entry(border_entry1, font=('Arial', 12, 'bold'), bd=10, bg='#615458', fg='#FAFAFF', relief=FLAT).grid(row=0, column=0, sticky=(E, W))

    # Jogador 2
    self.player2_image = PhotoImage(file=resource_path('./images/player2.png'))
    Label(mainframe, image=self.player2_image, bg='#6e5c62').grid(row=3, column=0, sticky=W, pady='15 0')
    
    border_entry2 = Frame(mainframe, bg='#312a2c', padx=3, pady=3)
    border_entry2.grid(row=4, column=0, sticky=(E, W))
    border_entry2.columnconfigure(0, weight=1)
    border_entry2.rowconfigure(0, weight=1)
    
    Entry(border_entry2, font=('Arial', 12, 'bold'), bd=10, bg='#615458', fg='#FAFAFF', relief=FLAT).grid(row=0, column=0, sticky=(E, W))

    # Botão Iniciar
    self.play_button_image = PhotoImage(file=resource_path('./images/play-button.png'))
    self.play_button_image_mouseover = PhotoImage(file=resource_path('./images/play-button-mouseover.png'))
    play_button = Label(mainframe, image=self.play_button_image, bg='#6e5c62', cursor='hand2')
    play_button.grid(row=5, column=0, sticky=S)
    play_button.bind('<Enter>', lambda _: play_button.config(image=self.play_button_image_mouseover))
    play_button.bind('<Leave>', lambda _: play_button.config(image=self.play_button_image))
    play_button.bind('<Button-1>', self.popup_game)

    for child in mainframe.winfo_children(): 
      child.grid_configure(padx=10)

  def open(self):
    self.controller.title("Termo - Main Menu")
    self.controller.geometry('700x500')
    self.controller.resizable(width=False, height=False)
    self.controller.columnconfigure(0, weight=1)
    self.controller.rowconfigure(0, weight=1)

  def popup_game(self, event):
    self.controller.show_frame(Game)