from src.Fighter_class.Fighter import FighterInterface
from src.Fighter_class.Class import Warrior, Rogue, Wizard, Priest
from src.Fighter_class.Team import Team
from src.db.insert_db import insert_fighter
from src.db.get_db import get_random_fighter, get_random_team
from src.db.update_db import set_hp_fighter
from src.misc.NameGenerator import name_generator
from random import randrange

class Game():
    teams : list[Team]
    fighters : list[FighterInterface]
    def __init__(self) -> None:
        #self.generate_new_fighter()
        self.fighters = self.get_figthers_from_db()
        self.teams = self.assign_team()

    def generate_new_fighter(self):
        """
        Generate 20 random fighters and insert them into the database
        """
        print("Génération de 20 nouveau combattants...")
        for i in range(20):
            name = name_generator()
            lastname = name_generator()
            choice = randrange(1,5)
            if choice == 1:
                attack = randrange(70,91)
                defense_value = randrange(70, 91)
                health_point = randrange(120, 151)
                critical = randrange(5,8)
                initiative = randrange(40,61)
                parry = randrange(40,61)
                player = Warrior(name, lastname, attack, defense_value, health_point, critical, initiative, parry)
            if choice == 2:
                attack = randrange(40,61)
                defense_value = randrange(30, 51)
                health_point = randrange(70, 81)
                critical = randrange(15,21)
                initiative = randrange(75,91)
                dodge = randrange(40,71)
                player = Rogue(name, lastname, attack, defense_value, health_point, critical, initiative, None, dodge)
            if choice == 3:
                attack = randrange(100,151)
                defense_value = randrange(20, 41)
                health_point = randrange(60, 71)
                critical = randrange(5,7)
                initiative = randrange(75,91)
                player = Wizard(name, lastname, attack, defense_value, health_point, critical, initiative)
            if choice == 4:
                attack = randrange(30,61)
                defense_value  = randrange(60, 81)
                health_point = randrange(70, 90)
                critical = randrange(5,7)
                initiative = randrange(50,60)
                parry = randrange(30,51)
                player = Priest(name, lastname, attack, defense_value, health_point, critical, initiative, parry)
        
            id = insert_fighter((player.name, player.lastname, player._class, player.attack_value, player.defense_value, player.health_point, player.critical, player.initiative, player.parry, player.dodge))

    def get_figthers_from_db(self):
        """
        Get 20 random fighters from the database
        """
        datas = get_random_fighter()
        fighters = list()

        for data in datas:
            if data[3] == 'warrior':
                fighter = Warrior(id = data[0], name = data[1], lastname = data[2], attack_value=data[4], defense_value=data[5], health_point=data[6], critical=data[7], initiative=data[8], parry=data[9], dodge=data[10])
            elif data[3] == 'Rogue':
                fighter = Rogue(id = data[0], name = data[1], lastname = data[2], attack_value=data[4], defense_value=data[5], health_point=data[6], critical=data[7], initiative=data[8], parry=data[9], dodge=data[10])
            elif data[3] == 'Wizard':
                fighter = Wizard(id = data[0], name = data[1], lastname = data[2], attack_value=data[4], defense_value=data[5], health_point=data[6], critical=data[7], initiative=data[8], parry=data[9], dodge=data[10])
            elif data[3] == 'Priest':
                fighter = Priest(id = data[0], name = data[1], lastname = data[2], attack_value=data[4], defense_value=data[5], health_point=data[6], critical=data[7], initiative=data[8], parry=data[9], dodge=data[10])
            fighters.append(fighter)

        return fighters

    def assign_team(self):
        """
        Assign 10 fighters in each teams
        """
        datas = get_random_team()
        teams = list()
        teams: list[Team]
        mid = self.fighters[10:]

        for data in datas:
            team = Team(id = data[0], name = data[1],fighters = mid)
            if team.name == "Blue":
                team.color = "\033[34m"
                self.team_blue_bk = team.fighters.copy()
            else:
                team.color = "\033[32m"
                self.team_red_bk = team.fighters.copy()

            mid = self.fighters[:10]
            teams.append(team)
        
        for fighter in self.fighters:
            if fighter in teams[0].fighters:
                fighter.set_enemy_team(teams[1].fighters)
                fighter.set_ally_team(teams[0].fighters)
                fighter.set_color(teams[0].color)

            else:
                fighter.set_enemy_team(teams[0].fighters)
                fighter.set_ally_team(teams[1].fighters)
                fighter.set_color(teams[1].color)
        
        return teams

    def update_fighter_in_db(self):
        f: FighterInterface
        for team in self.teams:
            if team.name == "Blue":
                for f in self.team_blue_bk:
                    if f in team.fighters:
                        set_hp_fighter((f.health_point, f.id))
                        #print("Vivant")
                    else:
                        set_hp_fighter((0, f.id))
                        #print("Dead")
            else:
                for f in self.team_red_bk:
                    if f in team.fighters:
                        set_hp_fighter((f.health_point, f.id))
                        #print("Vivant")
                    else:
                        set_hp_fighter((0, f.id))
                        #print("Dead")


    def do_fight(self):
        print("=================BATTLE START=================")
        for team in self.teams:
            team.team_str()
            

        print("")        

        for fighter in self.fighters:
            fighter.start()

        for fighter in self.fighters:
            fighter.join()

        print("")
        print("=================BATTLE END=================")
        for team in self.teams:
            team.team_str()
            print(f"=> Combattant(s) en vie: {team.fighters_alive()}/10")

        #self.update_fighter_in_db()

if __name__ == '__main__':
    game = Game()
    game.do_fight()
    