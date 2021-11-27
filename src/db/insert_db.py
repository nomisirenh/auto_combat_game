from db_conection import create_connection

def insert_fighter(values):

    querry = """INSERT INTO Fighter(name, lastname, class, attack_value, defense_value, health_point, critical, initiative, parry, dodge) 
                VALUES (?,?,?,?,?,?,?,?,?,?)"""
    
    conn = create_connection()
    with conn:
        c = conn.cursor()
        c.execute(querry, values)
        conn.commit()

if __name__ == '__main__':
    values = ('HS', 'lebrun', 'Warrior', 50, 51,42,53, 50, None, None)
    insert_fighter(values)