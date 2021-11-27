from db_conection import create_connection
from sqlite3 import Error

def create_table(querry):

    conn = create_connection()

    if conn is not None:
        with conn:
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
                            parry integer,
                            dodge integer
                        );"""

    sql_table_team = """CREATE TABLE IF NOT EXISTS Team (
                            team_id integer PRIMARY KEY AUTOINCREMENT,
                            name text NOT NULL
                        );"""

    sql_table_battle = """CREATE TABLE IF NOT EXISTS Battle (
                            battle_id integer PRIMARY KEY AUTOINCREMENT,
                            winner_team text
                            loser_team text
                            still_living int
                        );"""

    sql_table_fighter_team = """CREATE TABLE IF NOT EXISTS Fighter_team (
                            fighter_team_id integer PRIMARY KEY  AUTOINCREMENT,
                            fighter_id int NOT NULL,
                            team_id int NOT NULL,
                            battle_id int NOT NULL,
                            FOREIGN KEY (fighter_id) REFERENCES Fighter (fighter_id),
                            FOREIGN KEY (team_id) REFERENCES Team (team_id),
                            FOREIGN KEY (battle_id) REFERENCES Battle (battle_id)
                        );"""
    
    querries = [sql_table_fighter, sql_table_team, sql_table_battle, sql_table_fighter_team]

    for i in range(len(querries)):
        print(i)
        create_table(querries[i])

if __name__ == '__main__':
    main()
     