import sqlite3
from sqlite3 import Error


def create_connection():
    """ create a database connection to database """
    conn = None
    try:
        conn = sqlite3.connect(r"sql_lite.db")
        return conn
    except Error as e:
        print(e)



if __name__ == '__main__':
    conn = create_connection()
    if conn is not None:
        conn.close()
        