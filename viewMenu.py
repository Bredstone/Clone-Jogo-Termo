from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style
from viewJogo import *

class App(object):
  def __init__(self, master):
    self.root = master
    self.root.title("Termo - Main Menu")
    self.root.resizable(width=False, height=False)
    self.root.columnconfigure(0, weight=1)
    self.root.rowconfigure(0, weight=1)

    # Mainframe
    mainframe = Frame(master, width=700, height=500, bg='#6e5c62', padx=120, pady=45)
    mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.rowconfigure(5, weight=1)
    mainframe.grid_propagate(0)

    # Título
    self.title_image = PhotoImage(file='images/title.png')
    Label(mainframe, image=self.title_image, bg='#6e5c62').grid(row=0, column=0, sticky=(N, E, W))

    # Jogador 1
    self.player1_image = PhotoImage(file='images/player1.png')
    Label(mainframe, image=self.player1_image, bg='#6e5c62').grid(row=1, column=0, sticky=W)
    
    border_entry1 = Frame(mainframe, bg='#312a2c', padx=3, pady=3)
    border_entry1.grid(row=2, column=0, sticky=(E, W))
    border_entry1.columnconfigure(0, weight=1)
    border_entry1.rowconfigure(0, weight=1)
    
    Entry(border_entry1, font=('Arial', 12, 'bold'), bd=10, bg='#615458', fg='#FAFAFF', relief=FLAT).grid(row=0, column=0, sticky=(E, W))

    # Jogador 2
    self.player2_image = PhotoImage(file='images/player2.png')
    Label(mainframe, image=self.player2_image, bg='#6e5c62').grid(row=3, column=0, sticky=W, pady='15 0')
    
    border_entry2 = Frame(mainframe, bg='#312a2c', padx=3, pady=3)
    border_entry2.grid(row=4, column=0, sticky=(E, W))
    border_entry2.columnconfigure(0, weight=1)
    border_entry2.rowconfigure(0, weight=1)
    
    Entry(border_entry2, font=('Arial', 12, 'bold'), bd=10, bg='#615458', fg='#FAFAFF', relief=FLAT).grid(row=0, column=0, sticky=(E, W))

    # Botão Iniciar
    self.play_button_image = PhotoImage(file='images/play-button.png')
    self.play_button_image_mouseover = PhotoImage(file='images/play-button-mouseover.png')
    play_button = Label(mainframe, image=self.play_button_image, bg='#6e5c62', cursor='hand2')
    play_button.grid(row=5, column=0, sticky=S)
    play_button.bind('<Enter>', lambda _: play_button.config(image=self.play_button_image_mouseover))
    play_button.bind('<Leave>', lambda _: play_button.config(image=self.play_button_image))

    for child in mainframe.winfo_children(): 
      child.grid_configure(padx=10)

def initGUI(__name__):      

    if __name__ == "__menu__":
        root = Tk()
        m = App(root)
        root.mainloop()