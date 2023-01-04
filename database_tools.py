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
