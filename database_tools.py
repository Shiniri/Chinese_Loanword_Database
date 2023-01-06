import sqlite3
from sqlite3 import Error


def create_connection(path):

    connection = None

    try:
        connection = sqlite3.connect(path)
        print('Connection successful.')
    except Error as e:
        print(e)

    return connection


# type can be 'commit' or 'read'
def execute_query(connection, query, type):

    cursor = connection.cursor()

    if type == 'commit':
        try:
            cursor.execute(query)
            connection.commit()
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


def add_word(database_connection, information):
    add_word_query = f"""
        INSERT INTO loanwords (hanzi, pinyin, ipa, original_form, eng_translation, description)
        VALUES (\"{information[0]}\", 
                \"{information[1]}\",
                \"{information[2]}\",
                \"{information[3]}\",
                \"{information[4]}\",
                \"{information[5]}\");
        """
    execute_query(database_connection, add_word_query, 'commit')


def update_txt_from_database(database_connection):
    with open('loanwords.txt', 'w', encoding='utf8') as file:
        get_words_query = 'SELECT * FROM loanwords;'
        row_list = execute_query(database_connection, get_words_query, 'read')
        for word in row_list:
            for column in word:
                file.write(str(column) + ' ')
            file.write('\n')