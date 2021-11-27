from db_conection import create_connection

def insert_fighter(values):

    querry = """INSERT INTO Fighter(name, lastname, class, attack_value, defense_value, health_point, critical, initiative, parry, dodge) 
                VALUES (?,?,?,?,?,?,?,?,?,?)"""
    
    conn = create_connection()
    with conn:
        c = conn.cursor()
        c.execute(querry, values)
        conn.commit()
        return c.lastrowid

def insert_battle(values):

    querry = """INSERT INTO Battle(winner_team, loser_team, still_living) 
                VALUES (?,?,?)"""
    
    conn = create_connection()
    with conn:
        c = conn.cursor()
        c.execute(querry, values)
        conn.commit()
        return c.lastrowid

def insert_team(values):

    querry = """INSERT INTO Team(name) 
                VALUES (?)"""
    
    conn = create_connection()
    with conn:
        c = conn.cursor()
        c.execute(querry, values)
        conn.commit()
        return c.lastrowid

def insert_fighter_team(values):

    querry = """INSERT INTO Fighter_team(fighter_id, team_id ,battle_id) 
                VALUES (?,?,?)"""
    
    conn = create_connection()
    with conn:
        c = conn.cursor()
        c.execute(querry, values)
        conn.commit()
        return c.lastrowid

if __name__ == '__main__':
    values = ('HS', 'lebrun', 'Warrior', 50, 51,42,53, 50, None, None)
    id = insert_fighter(values)
    print(id)