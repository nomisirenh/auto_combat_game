from db_conection import create_connection
from sqlite3 import Error

def create_table(querry):

    conn = create_connection()

    if conn is not None:
        try:
            conn.cursor()
            conn.execute(querry)

        except Error as e:
            print(e)
    else:
        print("Can't create database connection")

def main():
    sql_table_fighter = """CREATE TABLE IF NOT EXISTS Fighter (
                            fighter_id integer PRIMARY KEY AUTOINCREMENT,
                            name text NOT NULL,
                            lastname text NOT NULL,
                            class text NOT NULL,
                            attack_value integer NOT NULL,
                            defense_value integer NOT NULL,
                            health_point integer NOT NULL,
                            critical integer NOT NULL,
                            initiative integer NOT NULL,
                            team integer NOT NULL,
                            parry integer,
                            dodge integer
                        ); """
                        
    create_table(sql_table_fighter)

if __name__ == '__main__':
    main()
    