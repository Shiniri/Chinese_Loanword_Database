#
#   TO_DO:
#       - add 'original form'-column
#       - make 'kafei' and 'xianzai' nicer
#


from tkinter import *
from tkinter import ttk


import database_tools


class Database_Window(Tk):

    def __init__(self):
        super().__init__()

        # database #
        self.database_connection = database_tools.create_connection('loanwords.db')
        self.listbox_content = self.get_listbox_contents()

        # GUI #
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
        for word in self.listbox_content:
                loanword_listbox.insert(word[0], word[1:])
        loanword_listbox.pack()

        # searchbar #
        search_bar = Entry(self, width=300)
        search_bar.pack()

        # information window #
        information_window = Label(self, width=300)
        information_window.pack()

    def get_listbox_contents(self):
        read_words_query = 'SELECT * FROM loanwords;'
        columns = database_tools.execute_query(self.database_connection, read_words_query, 'read')

        return columns
        

if __name__ == "__main__":
    window = Database_Window()
    window.mainloop()
