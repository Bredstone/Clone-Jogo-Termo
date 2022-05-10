import string
from tkinter import *

from pathResolver import resource_path

class Game(Frame):
  def __init__(self, parent, controller):
    Frame.__init__(self, parent)
    self.controller = controller
    self.root = self

    # Mainframe
    mainframe = Frame(self.root, width=700, height=800, bg='#6e5c62', padx=120, pady=45)
    mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(2, weight=1)
    mainframe.grid_propagate(0)

    # Título
    self.title_image = PhotoImage(file=resource_path('./images/title.png'))
    Label(mainframe, image=self.title_image, bg='#6e5c62').grid(row=0, column=0, sticky=(N, E, W))

    # Jogador 1
    score_player1 = Frame(mainframe, bg='#6e5c62')
    score_player1.grid(column=0, row=1, sticky=W, pady='35 0')
    score_player1.columnconfigure(0, weight=1)

    self.player1_image = PhotoImage(file=resource_path('./images/player1.png'))
    Label(score_player1, image=self.player1_image, bg='#6e5c62').grid(row=0, column=0)
    Label(score_player1, text="999", font=('Fira Code', 15, 'bold'), bg='#6e5c62', fg="#FAFAFF").grid(row=1, column=0)

    # Jogador 2
    score_player2 = Frame(mainframe, bg='#6e5c62')
    score_player2.grid(column=0, row=1, sticky=E, pady='35 0')
    score_player2.columnconfigure(0, weight=1)

    self.player2_image = PhotoImage(file=resource_path('./images/player2.png'))
    Label(score_player2, image=self.player2_image, bg='#6e5c62').grid(row=0, column=0)
    Label(score_player2, text="999", font=('Fira Code', 15, 'bold'), bg='#6e5c62', fg="#FAFAFF").grid(row=1, column=0)

    # Tabuleiro
    self.init_board_images()

    board_frame = Frame(mainframe, bg='#6e5c62')
    board_frame.grid(column=0, row=2)
    self.board = [[0] * 5 for _ in range(6)]
    for row in range(6):
      for column in range(5):
        self.board[row][column] = Label(board_frame, image=self.empty[''], bg='#6e5c62', fg="white")
        self.board[row][column].grid(row=row, column=column)

    for child in mainframe.winfo_children(): 
      child.grid_configure(padx=10)

  def open(self):
    self.controller.title("Termo - Game")
    self.controller.geometry('700x800')
    self.controller.resizable(width=False, height=False)
    self.controller.columnconfigure(0, weight=1)
    self.controller.rowconfigure(0, weight=1)

    self.cur_row = 0
    self.cur_column = 0
    self.root.focus_set()
    self.root.bind('<Key>', self.take_input)

  def init_board_images(self):
    self.empty = {'': PhotoImage(file=resource_path('./images/empty-tile.png'))}
    for letter in string.ascii_lowercase:
      self.empty[letter] = PhotoImage(file=resource_path(f'./images/empty-tile-{letter}.png'))
  
  def take_input(self, event):
    if event.char.lower() in list(string.ascii_lowercase) and self.cur_column < 5:
      self.board[self.cur_row][self.cur_column].config(image=self.empty[event.char.lower()])
      self.cur_column += 1
    elif event.char == '\x08':
      self.cur_column = max(0, self.cur_column - 1)
      self.board[self.cur_row][self.cur_column].config(image=self.empty[''])
    else:
      pass