from src.Fighter_class.Fighter import FighterInterface
from src.Fighter_class.Class import Warrior, Rogue, Wizard, Priest
from src.db.insert_db import insert_fighter
from src.db.get_db import get_random_fighter
from src.Fighter_class.NameGenerator import name_generator
from random import randrange

class Game():
    def __init__(self) -> None:
        pass

    def generate_new_fighter(self):
        """
        Will generate 20 random fighters and insert them into the database
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

    def get_figthers(self):
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


if __name__ == '__main__':
    g = Game()
    datas = g.get_figthers()
    data : FighterInterface
    for data in datas:
        print(data)