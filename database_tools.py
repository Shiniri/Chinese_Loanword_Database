import sqlite3
from sqlite3 import Error


class Database_Tools():
    def __init__(self):
        self.database_path = 'chinese_loanword_database.db'
        self.connection_to_database = self.create_connection()
        self.loanword_txt = 'loanword.txt'
    

    def create_connection(self):

        try:
            connection = sqlite3.connect(self.database_path)
            print('Connection successful.')
        except Error as e:
            print(e)

        return connection


    # type can be 'commit' or 'read'
    def execute_query(self, query, type):

        cursor = self.connection_to_database.cursor()

        if type == 'commit':
            try:
                cursor.execute(query)
                self.connection_to_database.commit()
                print('Success.')
            except Error as e:
                print(e)
        elif type == 'read':
            result = None
            try:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
            except Error as e:
                print(e)    


    def create_table(self):
        create_table_query = """
            CREATE TABLE IF NOT EXISTS loanwords (
                word_id INTEGER PRIMARY KEY AUTOINCREMENT,
                hanzi TEXT NOT NULL,
                pinyin TEXT NOT NULL,
                original_representation TEXT NOT NULL,
                eng_translation TEXT NOT NULL,
                donor TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT NOT NULL)
            """
        self.execute_query(create_table_query, 'commit')


    def add_word(self, information):
        add_word_query = f"""
            INSERT INTO loanwords (hanzi, pinyin, original_representation, eng_translation, donor, category, description)
            VALUES (\"{information[0]}\", 
                    \"{information[1]}\",
                    \"{information[2]}\",
                    \"{information[3]}\",
                    \"{information[4]}\",
                    \"{information[5]}\",
                    \"{information[6]}\");
            """
        self.execute_query(add_word_query, 'commit')

    
    def update_txt_from_database(self):
        with open(self.loanword_txt, 'w', encoding='utf8') as file:
            get_words_query = 'SELECT * FROM loanwords;'
            row_list = self.execute_query(get_words_query, 'read')

            file.write('HANZI | PINYIN | ORIGINAL FORM | ENGLISH TRANSLATION |  DONOR | CATEGORY | DESCRIPTION \n')

            for word in row_list:
                for column in word:
                    file.write(str(column) + ' ')
                file.write('\n')
