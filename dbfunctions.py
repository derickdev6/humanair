import sqlite3


def create(sql_sentence):
    # Connects to DB
    sqliteConnection = sqlite3.connect('humanairDB.sqlite')
    cursor = sqliteConnection.cursor()
    # Print statement and execution
    cursor.execute(sql_sentence)
    sqliteConnection.commit()
    if cursor.rowcount > 0:
        print(f'succesfully created {cursor.rowcount} items')
    # cursor.close()
    return True if cursor.rowcount > 0 else False


def read(sql_sentence, *single):
    # Connects to DB
    sqliteConnection = sqlite3.connect('humanairDB.sqlite')
    cursor = sqliteConnection.cursor()
    # Print statement and execution
    if single:
        print("Single")
        cursor.execute(sql_sentence)
        # cursor.close()
        return cursor.fetchone()
    else:
        print("Multiple")
        cursor.execute(sql_sentence)
        # cursor.close()
        return cursor.fetchall()


def update():
    pass


def delete():
    pass