from tkinter import *
import string

from controller import Termo

class Game(Frame):
  def __init__(self, parent_container, parent):
    Frame.__init__(self, parent_container)
    self.parent = parent
    self.root = self

    # Mainframe
    mainframe = Frame(self.root, width=700, height=850, bg='#6e5c62', padx=120, pady=45)
    mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(2, weight=1)
    mainframe.grid_propagate(0)

    # Título
    self.title_image = PhotoImage(file='images/title.png')
    Label(mainframe, image=self.title_image, bg='#6e5c62').grid(row=0, column=0, sticky=(N, E, W))

    # Jogador 1
    score_player1 = Frame(mainframe, bg='#6e5c62')
    score_player1.grid(column=0, row=1, sticky=W, pady='35 0')
    score_player1.columnconfigure(0, weight=1)

    self.player1_name = Label(score_player1, font=('Fira Code', 20, 'bold'), bg='#6e5c62', fg="#FAFAFF")
    self.player1_name.grid(row=0, column=0, sticky=W)
    self.player1_score = Label(score_player1, text="000", font=('Fira Code', 15, 'bold'), bg='#6e5c62', fg="#FAFAFF")
    self.player1_score.grid(row=1, column=0, sticky=W)

    # Jogador 2
    score_player2 = Frame(mainframe, bg='#6e5c62')
    score_player2.grid(column=0, row=1, sticky=E, pady='35 0')
    score_player2.columnconfigure(0, weight=1)

    self.player2_name = Label(score_player2, font=('Fira Code', 20, 'bold'), bg='#6e5c62', fg="#FAFAFF")
    self.player2_name.grid(row=0, column=0, sticky=E)
    self.player2_score = Label(score_player2, text="000", font=('Fira Code', 15, 'bold'), bg='#6e5c62', fg="#FAFAFF")
    self.player2_score.grid(row=1, column=0, sticky=E)

    # Warnings
    self.warnings = []

    # Palavras devem ter 5 letras
    self.five_letters_warning_image = PhotoImage(file='images/five-letters-warning.png')
    self.warnings.append(Label(mainframe, image=self.five_letters_warning_image, bg='#6e5c62'))

    # Palavra não reconhecida
    self.invalid_word_warning_image = PhotoImage(file='images/invalid-word-warning.png')
    self.warnings.append(Label(mainframe, image=self.invalid_word_warning_image, bg='#6e5c62'))

    # Palavra certa
    self.correct_word_warning_image = PhotoImage(file='images/correct-word-warning.png')
    self.warnings.append(Label(mainframe, image=self.correct_word_warning_image, bg='#6e5c62'))

    # Empate
    self.draw_warning_image = PhotoImage(file='images/draw-warning.png')
    self.warnings.append(Label(mainframe, image=self.draw_warning_image, bg='#6e5c62'))

    # Tabuleiro
    self.initBoardImages()

    board_frame = Frame(mainframe, bg='#6e5c62')
    board_frame.grid(column=0, row=2, sticky=N, pady='65 0')
    self.board = [[0] * 5 for _ in range(6)]
    self.board_value = [[''] * 5 for _ in range(6)]
    for row in range(6):
      for column in range(5):
        self.board[row][column] = Label(board_frame, image=self.empty[''], bg='#6e5c62', fg="white")
        self.board[row][column].grid(row=row, column=column)

    self.end_message_word = Label(
      mainframe, 
      text='A palavra correta era ""', 
      font=('Fira Code', 16, 'bold'), 
      bg='#6e5c62', 
      fg="#FAFAFF"
    )

    self.end_message = Label(
      mainframe, 
      text='Pressione <Enter> para jogar novamente ou <Esc> para sair.', 
      font=('Fira Code', 12, 'bold'), 
      bg='#6e5c62', 
      fg="#FAFAFF"
    )

    for child in mainframe.winfo_children(): 
      child.grid_configure(padx=10)

  def open(self, player1_name, player2_name):
    self.parent.title("Termo - Game")
    self.parent.geometry('700x850')
    self.parent.resizable(width=False, height=False)
    self.parent.columnconfigure(0, weight=1)
    self.parent.rowconfigure(0, weight=1)

    self.player1_name.config(text=player1_name.upper())
    self.player2_name.config(text=player2_name.upper())

    self.controller = Termo(player1_name, player2_name, self)
    self.controller.novaPartida()

    self.resetBoard()

  def initBoardImages(self):
    self.empty = {
      '': PhotoImage(file='images/empty-tile/empty-tile.png'), 
      'selected-row': PhotoImage(file='images/empty-tile/empty-tile-selected-row.png'),
      'selected-tile': PhotoImage(file='images/empty-tile/empty-tile-selected-tile.png'),
      }
    self.right = dict()
    self.semi_correct = dict()
    self.wrong = dict()

    for letter in string.ascii_lowercase:
      self.empty[letter] = PhotoImage(file=f'images/empty-tile/empty-tile-{letter}.png')

    for letter in string.ascii_lowercase + 'áéíóúâêôãõç':
      self.right[letter] = PhotoImage(file=f'images/right-tile/right-tile-{letter}.png')
      self.semi_correct[letter] = PhotoImage(file=f'images/semi-correct-tile/semi-correct-{letter}.png')
      self.wrong[letter] = PhotoImage(file=f'images/wrong-tile/wrong-tile-{letter}.png')

  def refreshScore(self, scorePlayer1, scorePlayer2):
    self.player1_score.config(text=f'{scorePlayer1:03d}')
    self.player2_score.config(text=f'{scorePlayer2:03d}')

  def setCurPlayer(self, player):
    self.player1_name.config(fg='#FAFAFF')
    self.player2_name.config(fg='#FAFAFF')
    self.player1_score.config(fg='#FAFAFF')
    self.player2_score.config(fg='#FAFAFF')
    
    if player == 0:
      self.player1_name.config(fg='#D3AD69')
      self.player1_score.config(fg='#D3AD69')
    else: 
      self.player2_name.config(fg='#D3AD69')
      self.player2_score.config(fg='#D3AD69')

  def showNotification(self, code, autoFade=True):
    self.warnings[code].place(relx=0.5, y=210, anchor=CENTER)
    if autoFade:
      self.warnings[code].after(1500, lambda: self.warnings[code].place_forget())
  
  def notifyWinner(self, player, word, rightWord=True):
    self.showNotification(3 if player == 2 else 2, False)

    self.player1_name.config(fg='#FAFAFF')
    self.player1_score.config(fg='#FAFAFF')
    self.player2_name.config(fg='#FAFAFF')
    self.player2_score.config(fg='#FAFAFF')

    if player == 0 or player == 2:
      self.player1_name.config(fg='#3AA394')
      self.player1_score.config(fg='#3AA394')
    
    if player == 1 or player == 2: 
      self.player2_name.config(fg='#3AA394')
      self.player2_score.config(fg='#3AA394')

    if rightWord:
      self.player1_score.config(text='---')
      self.player2_score.config(text='---')

      if self.cur_row < 6:
        [tile.config(image=self.empty['']) for tile in self.board[self.cur_row]]
    
    self.root.unbind('<Key>')
    self.root.bind('<Key>', self.endGame)

    self.end_message_word.config(text=f'A palavra correta era "{word.upper()}"')
    self.end_message_word.place(relx=0.5, rely=0.95, anchor=CENTER)
    self.end_message.place(relx=0.5, rely=1, anchor=CENTER)

  def endGame(self, keyPress):
    if keyPress.keysym == 'Return':
      self.resetBoard()
      self.controller.novaPartida()
    elif keyPress.keysym == 'Escape':
      self.parent.destroy()

  def takeInput(self, keyPress):
    if keyPress.char.lower() in list(string.ascii_lowercase) and self.cur_column < 5:
      self.board[self.cur_row][self.cur_column].config(image=self.empty[keyPress.char.lower()])
      self.board_value[self.cur_row][self.cur_column] = keyPress.char.lower()

      self.cur_column += 1

      if self.cur_column < 5:
        self.board[self.cur_row][self.cur_column].config(image=self.empty['selected-tile'])
    elif keyPress.char == '\x08':
      if self.cur_column < 5:
        self.board[self.cur_row][self.cur_column].config(image=self.empty['selected-row'])

      self.cur_column = max(0, self.cur_column - 1)

      self.board[self.cur_row][self.cur_column].config(image=self.empty['selected-tile'])
      self.board_value[self.cur_row][self.cur_column] = ''
    elif keyPress.keysym == 'Return':
      if self.cur_column != 5:
        self.showNotification(0)
      else:
        self.controller.verifyEntry(''.join(self.board_value[self.cur_row]))
    else:
      pass

  def resetBoard(self):
    [warning.grid_forget() for warning in self.warnings]
    [warning.place_forget() for warning in self.warnings]
    self.end_message.grid_forget()
    self.end_message_word.grid_forget()
    self.end_message.place_forget()
    self.end_message_word.place_forget()

    self.root.focus_set()
    self.root.unbind('<Key>')
    self.root.bind('<Key>', self.takeInput)

    self.cur_row = 0
    self.cur_column = 0

    for row in range(6):
      for column in range(5):
        self.board[row][column].config(image=self.empty[''])
        self.board_value[row][column] = ''

    [tile.config(image=self.empty['selected-row']) for tile in self.board[self.cur_row]]
    self.board[self.cur_row][self.cur_column].config(image=self.empty['selected-tile'])

  def refreshBoard(self, hit_list, word):
    for i in range(len(hit_list)):
      if hit_list[i] == 10:
        self.board[self.cur_row][i].config(image=self.right[word[i]])
      elif hit_list[i] == 5:
        self.board[self.cur_row][i].config(image=self.semi_correct[word[i]])
      else:
        self.board[self.cur_row][i].config(image=self.wrong[word[i]])
    
    self.cur_row += 1
    self.cur_column = 0

    if self.cur_row < 6:
      [tile.config(image=self.empty['selected-row']) for tile in self.board[self.cur_row]]
      self.board[self.cur_row][self.cur_column].config(image=self.empty['selected-tile'])