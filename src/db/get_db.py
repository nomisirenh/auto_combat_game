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

def get_history(battle_id):
    sql_querry = """ SELECT Fighter.fighter_id, Fighter.class, Fighter.name, Fighter.lastname,Team.name, Fighter_team.remaining_hp,Fighter_team.fighting_tactic, Fighter_team.healing_tactic,Battle.winner_team, Battle.loser_team
                    from Fighter
                    INNER JOIN Fighter_team On Fighter_team.fighter_id = Fighter.fighter_id
                    INNER JOIN Battle ON Battle.battle_id = Fighter_team.battle_id
                    Inner JOIN Team ON Team.team_id = Fighter_team.team_id
                    WHERE Battle.battle_id = ?
                    """

    conn = create_connection()
    with conn:
        c = conn.cursor()
        c.execute(sql_querry, (battle_id,))

        datas = c.fetchall()
        return datas

def get_max_battle_id():
    sql_querry = """ SELECT max(battle_id) from Battle
                    """

    conn = create_connection()
    with conn:
        c = conn.cursor()
        c.execute(sql_querry)

        datas = c.fetchall()
        return datas[0][0]
