from Fighter import FighterInterface
from random import randrange

class Warrior(FighterInterface):
    def __init__(self, name, lastname, attack_value = randrange(70,91), defense_value = randrange(70, 91), health_point = randrange(120, 151), critical = randrange(5,8), initiative = randrange(40,61), parry = randrange(40,61)):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative)
        self.parry = parry

    def attack_maneuver(self):
        return super().attack_maneuver()


if __name__ == '__main__':
    warrior = Warrior("HS", "Lebrun")
    print(warrior.name)
    print(warrior.attack_value)
    print(warrior.defense_value)
    print(warrior.parry)