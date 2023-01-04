import sqlite3
from sqlite3 import Error


def create_connection(path):

    connection = None

    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful.")
    except Error as e:
        print(e)

    return connection


def execute_query(connection, query):

    cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()
        print("Success.")
    except Error as e:
        print(e)


def execute_read_query(connection, query):
    
    cursor = connection.cursor()
    result = None

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(e)


if __name__ == "__main__":

    connection = create_connection("C:\\Users\\49151\\Desktop\\Chinese_Loanword_Database\\test.db")

    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        nationality TEXT
    );
    """

    create_users = """
    INSERT INTO
        users (name, age, gender, nationality)
    VALUES
        ('James', 25, 'male', 'USA'),
        ('Leila', 32, 'female', 'France');
    """

    execute_query(connection, create_users_table)
    execute_query(connection, create_users)

    select_users = "SELECT * from users"
    users = execute_read_query(connection, select_users)

    for user in users:
        print(user)

    print("just to test commits")
