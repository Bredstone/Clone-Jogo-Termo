from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style

class App(object):
  def __init__(self, master):
    self.root = master
    self.root.title("Termo - Game")
    self.root.resizable(width=False, height=False)
    self.root.columnconfigure(0, weight=1)
    self.root.rowconfigure(0, weight=1)

    # Mainframe
    mainframe = Frame(master, width=700, height=900, bg='#6e5c62', padx=120, pady=45)
    mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(9, weight=1)
    mainframe.grid_propagate(0)

    # Título
    self.title_image = PhotoImage(file='images/title.png')
    Label(mainframe, image=self.title_image, bg='#6e5c62').grid(row=0, column=0, sticky=(N, E, W))

    # Jogador 1
    Label(mainframe, text="Breno", font=('Arial', 16, 'bold'), bg='#6e5c62', fg="white").grid(row=1, column=0, sticky=W)


    # Pontuação Jogador 1
    Label(mainframe, text="999", font=('Arial', 16, 'bold'), bg='#6e5c62', fg="white").grid(row=2, column=0, sticky=W)

    # Jogador 2
    Label(mainframe, text="Brendon", font=('Arial', 16, 'bold'), bg='#6e5c62', fg="white").grid(row=1, column=0, sticky=E)

    # Pontuação Jogador 1
    Label(mainframe, text="999", font=('Arial', 16, 'bold'), bg='#6e5c62', fg="white").grid(row=2, column=0, sticky=E)

    for child in mainframe.winfo_children(): 
      child.grid_configure(padx=10)

if __name__ == "__main__":
    root = Tk()
    m = App(root)
    root.mainloop()