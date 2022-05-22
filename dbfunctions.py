import sqlite3


def create():
    pass


def read(sql_sentence, *single):
    # Connects to DB
    sqliteConnection = sqlite3.connect('humanairDB.sqlite')
    cursor = sqliteConnection.cursor()
    # Print statement and execution
    if single:
        print("Single user")
        cursor.execute(sql_sentence)
        return cursor.fetchone()
    else:
        print("Multiple user")
        cursor.execute(sql_sentence)
        return cursor.fetchall()


def update():
    pass


def delete():
    pass