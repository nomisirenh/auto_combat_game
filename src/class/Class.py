from Fighter import FighterInterface
from random import randrange
from NameGenerator import name_generator

class Warrior(FighterInterface):
    def __init__(self, name = name_generator(), lastname = name_generator(), attack_value = randrange(70,91), defense_value = randrange(70, 91), health_point = randrange(120, 151), critical = randrange(5,8), initiative = randrange(40,61), parry = randrange(40,61)):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative)
        self.parry = parry

    def attack_maneuver(self):
        return super().attack_maneuver()

class Rogue(FighterInterface):
    def __init__(self, name = name_generator(), lastname = name_generator(), attack_value = randrange(40,61), defense_value = randrange(30, 51), health_point = randrange(70, 81), critical = randrange(15,21), initiative = randrange(75,91), dodge = randrange(40,71)):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative)
        self.dodge = dodge

    def attack_maneuver(self):
        return super().attack_maneuver()

class Wizard(FighterInterface):
    def __init__(self, name = name_generator(), lastname = name_generator(), attack_value = randrange(100,151), defense_value = randrange(20, 41), health_point = randrange(60, 71), critical = randrange(5,7), initiative = randrange(75,91)):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative)

    def attack_maneuver(self):
        return super().attack_maneuver()

class Priest(FighterInterface):
    def __init__(self, name = name_generator(), lastname = name_generator(), attack_value = randrange(30,61), defense_value = randrange(60, 81), health_point = randrange(70, 90), critical = randrange(5,7), initiative = randrange(50,60), parry = randrange(30,51)):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative)
        self.parry = parry

    def attack_maneuver(self):
        return super().attack_maneuver()


if __name__ == '__main__':
    warrior = Warrior()
    rogue = Rogue()
    wizard = Wizard()
    priest = Priest()

    