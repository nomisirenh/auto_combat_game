from src.db.db_connection import create_connection

def set_hp_fighter(data):
    sql_querry = """ UPDATE Fighter
                    SET health_point = ?
                    WHERE fighter_id = ?
                """
    
    conn = create_connection()
    with conn:
        c = conn.cursor()
        c.execute(sql_querry, data)
        conn.commit()
