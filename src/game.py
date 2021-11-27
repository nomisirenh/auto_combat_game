from src.Fighter_class.Class import Warrior, Rogue, Wizard, Priest
from src.db.insert_db import insert_fighter
from src.Fighter_class.NameGenerator import name_generator
from random import randrange

class Game():
    def __init__(self) -> None:
        pass

    def generate_fighter(self):
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

if __name__ == '__main__':
    g = Game()
    g.generate_fighter()