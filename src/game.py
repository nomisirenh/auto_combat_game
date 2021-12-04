from os import SEEK_CUR
from src.Fighter_class.Fighter import FighterInterface
from src.Fighter_class.Class import Warrior, Rogue, Wizard, Priest
from src.Fighter_class.Team import Team
from src.db.insert_db import insert_fighter
from src.db.get_db import get_random_fighter, get_random_team
from src.Fighter_class.NameGenerator import name_generator
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
                player = Warrior(name, lastname)
            if choice == 2:
                player = Rogue(name, lastname)
            if choice == 3:
                player = Wizard(name, lastname)
            if choice == 4:
                player = Priest(name, lastname)
        
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
        mid = self.fighters[10:]

        for data in datas:
            team = Team(id = data[0], name = data[1],fighters = mid)
            mid = self.fighters[:10]
            teams.append(team)
        
        return teams

    def do_fight(self):
        print("=================BATTLE START=================")
        for team in self.teams:
            team.team_str()
            

        print("")
        for fighter in self.fighters:
            if fighter in self.teams[0].fighters:
                fighter.set_enemy_team(self.teams[1].fighters)
                fighter.set_ally_team(self.teams[0].fighters)
            else:
                fighter.set_enemy_team(self.teams[0].fighters)
                fighter.set_ally_team(self.teams[1].fighters)

        for fighter in self.fighters:
            fighter.start()

        for fighter in self.fighters:
            fighter.join()

        print("")
        print("=================BATTLE END=================")
        for team in self.teams:
            team.team_str()
            print(f"Combattant(s) en vie: {team.fighters_alive()}/10")

if __name__ == '__main__':
    game = Game()
    game.do_fight()