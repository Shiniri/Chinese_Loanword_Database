from tkinter import *
from tkinter import ttk


class Database_Window(Tk):

    def __init__(self):
        super().__init__()
        self.geometry('300x400')
        self.resizable(0, 0)
        self.title('Chinese Loanwords')
        self.create_widgets()

    def create_widgets(self):
        # menubar #
        menubar = Menu(self)
        menubar.add_command(label='Language')
        menubar.add_command(label='Help')
        menubar.add_command(label='Add Word')
        self.config(menu=menubar)

        # listbox #
        loanword_listbox = Listbox(self, width=300)
        loanword_listbox.insert(1, '現在 | xiànzài | now | Sanskrit')
        loanword_listbox.pack()

        # searchbar #
        search_bar = Entry(self, width=300)
        search_bar.pack()

        # information window #
        information_window = Label(self, width=300)
        information_window.pack()
        