import sqlite3


def create():
    pass


def read(sql_sentence, *single):
    # Connects to DB
    sqliteConnection = sqlite3.connect('humanairDB.sqlite')
    cursor = sqliteConnection.cursor()
    # Print statement and execution
    if single:
        print("Single")
        cursor.execute(sql_sentence)
        return cursor.fetchone()
    else:
        print("Multiple")
        cursor.execute(sql_sentence)
        return cursor.fetchall()


def update():
    pass


def delete():
    pass