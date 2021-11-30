from src.db.db_conection import create_connection

def get_random_fighter():
    sql_querry = """ SELECT * FROM Fighter
                    ORDER BY random() LIMIT 20
                """
    
    conn = create_connection()
    with conn:
        c = conn.cursor()
        c.execute(sql_querry)

        datas = c.fetchall()
        return datas

if __name__ == '__main__':
    datas = get_random_fighter()
    for datas in datas:
        print(datas[3])