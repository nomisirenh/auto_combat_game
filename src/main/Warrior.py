from Fighter import FighterInterface
from random import randrange
from NameGenerator import name_generator

class Warrior(FighterInterface):
    def __init__(self, name = name_generator(), lastname = name_generator(), attack_value = randrange(70,91), defense_value = randrange(70, 91), health_point = randrange(120, 151), critical = randrange(5,8), initiative = randrange(40,61), parry = randrange(40,61)):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative)
        self.parry = parry

    def attack_maneuver(self):
        return super().attack_maneuver()


if __name__ == '__main__':
    warrior = Warrior()
    print(warrior.name)
    print(warrior.lastname)
    print(warrior.attack_value)
    print(warrior.defense_value)
    print(warrior.parry)