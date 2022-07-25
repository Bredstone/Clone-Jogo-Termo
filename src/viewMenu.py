from tkinter import *

from viewJogo import Game
from pathResolver import resource_path

class MainMenu(Frame):
  def __init__(self, parent_container, parent):
    Frame.__init__(self, parent_container)
    self.parent = parent
    self.root = self

    # Mainframe
    mainframe = Frame(self.root, width=700, height=500, bg='#6e5c62', padx=120, pady=45)
    mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.rowconfigure(5, weight=1)
    mainframe.grid_propagate(0)

    # Título
    self.title_image = PhotoImage(file=resource_path('images/title.png'))
    Label(mainframe, image=self.title_image, bg='#6e5c62').grid(row=0, column=0, sticky=(N, E, W))

    # Jogador 1
    self.player1_image = PhotoImage(file=resource_path('images/player1.png'))
    Label(mainframe, image=self.player1_image, bg='#6e5c62').grid(row=1, column=0, sticky=W)
    
    border_entry1 = Frame(mainframe, bg='#312a2c', padx=3, pady=3)
    border_entry1.grid(row=2, column=0, sticky=(E, W))
    border_entry1.columnconfigure(0, weight=1)
    border_entry1.rowconfigure(0, weight=1)
    
    self.player1_name = StringVar()
    Entry(border_entry1, font=('Arial', 12, 'bold'), bd=10, bg='#615458', fg='#FAFAFF', relief=FLAT, textvariable=self.player1_name).grid(row=0, column=0, sticky=(E, W))

    # Jogador 2
    self.player2_image = PhotoImage(file=resource_path('images/player2.png'))
    Label(mainframe, image=self.player2_image, bg='#6e5c62').grid(row=3, column=0, sticky=W, pady='15 0')
    
    border_entry2 = Frame(mainframe, bg='#312a2c', padx=3, pady=3)
    border_entry2.grid(row=4, column=0, sticky=(E, W))
    border_entry2.columnconfigure(0, weight=1)
    border_entry2.rowconfigure(0, weight=1)
    
    self.player2_name = StringVar()
    Entry(border_entry2, font=('Arial', 12, 'bold'), bd=10, bg='#615458', fg='#FAFAFF', relief=FLAT, textvariable=self.player2_name).grid(row=0, column=0, sticky=(E, W))

    # Warning
    self.names_warning_image = PhotoImage(file=resource_path('images/empty-names-warning.png'))
    self.names_warning = Label(mainframe, image=self.names_warning_image, bg='#6e5c62')

    # Botão Iniciar
    self.play_button_image = PhotoImage(file=resource_path('images/play-button.png'))
    self.play_button_image_mouseover = PhotoImage(file=resource_path('images/play-button-mouseover.png'))
    play_button = Label(mainframe, image=self.play_button_image, bg='#6e5c62', cursor='hand2')
    play_button.grid(row=5, column=0, sticky=S)
    play_button.bind('<Enter>', lambda _: play_button.config(image=self.play_button_image_mouseover))
    play_button.bind('<Leave>', lambda _: play_button.config(image=self.play_button_image))
    play_button.bind('<Button-1>', self.popupGame)
    
    self.parent.bind('<Return>', self.popupGame)

    for child in mainframe.winfo_children(): 
      child.grid_configure(padx=10)

  def open(self):
    self.parent.title("Termo - Main Menu")
    self.parent.geometry('700x500')
    self.parent.resizable(width=False, height=False)
    self.parent.columnconfigure(0, weight=1)
    self.parent.rowconfigure(0, weight=1)
    
    self.names_warning.grid_forget()

  def popupGame(self, event):
    if not self.player1_name.get() or not self.player2_name.get():
      self.names_warning.place(relx=0.5, y=95, anchor=CENTER)
      self.names_warning.after(1500, lambda: self.names_warning.place_forget())
    else:
      self.parent.unbind('<Return>')
      self.parent.game.tkraise()
      self.parent.game.open(self.player1_name.get(), self.player2_name.get())