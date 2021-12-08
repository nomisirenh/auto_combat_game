from src.db.db_connection import create_connection

def get_random_fighter():
    sql_querry = """ SELECT * FROM Fighter
                    WHERE health_point > 0
                    ORDER BY random() LIMIT 20
                """
    
    conn = create_connection()
    with conn:
        c = conn.cursor()
        c.execute(sql_querry)

        datas = c.fetchall()
        return datas

def get_random_team():
    sql_querry = """ SELECT * FROM Team
                     ORDER BY random()
                    """

    conn = create_connection()
    with conn:
        c = conn.cursor()
        c.execute(sql_querry)

        datas = c.fetchall()
        return datas
